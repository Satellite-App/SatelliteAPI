from typing import List, Union
from uuid import UUID
from pydantic import TypeAdapter

from core.config import Settings
from repositories import BaseMongoRepository
from models.token import Token


class TokenRepository(BaseMongoRepository):
    def __init__(self, settings: Settings):
        super().__init__(settings)
        self.database = self.database['tokens']

    async def get(self, _id: UUID) -> Union[Token, None]:
        token = await self.database.find_one({"_id": _id})
        if token is None:
            return None
        return Token.model_validate(token)

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Token]:
        tokens = await self.database.find(limit=limit, skip=skip).to_list(None)
        tokens_data = TypeAdapter(List[Token])
        return tokens_data.validate_python(tokens)

    async def create(self, token: Token) -> Token:
        token_id = await self.database.insert_one(token.model_dump(by_alias=True))
        token = await self.database.find_one({"_id": token_id.inserted_id})
        return Token.model_validate(token)

    async def delete(self, _id: UUID) -> int:
        delete_result = await self.database.delete_one({"_id": _id})
        return delete_result.deleted_count
