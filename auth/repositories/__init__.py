import logging

from motor.motor_asyncio import AsyncIOMotorClient

from core.config import Settings

logger = logging.getLogger(__name__)


class BaseMongoRepository:
    def __init__(self, settings: Settings):
        logger.info('Init connection to mongo')
        mongodb_client = AsyncIOMotorClient(settings.db_url, uuidRepresentation='standard')
        if mongodb_client.is_primary:
            logger.info('Connected to mongo')

        self.database = mongodb_client[settings.DB_NAME]
