import grpc
from concurrent import futures
import signal
import threading
import logging

logger = logging.getLogger(__name__)


class GRPCServer:
    def __init__(self, port: int, max_workers: int):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        self.port = port
        self._stop_event = threading.Event()

    def start(self):
        self.server.add_insecure_port(f'[::]:{self.port}')
        self.server.start()
        logger.info(f'Run server at {self.port}')

        signal.signal(signal.SIGINT, self._graceful_shutdown)
        signal.signal(signal.SIGTERM, self._graceful_shutdown)

        self.server.wait_for_termination()

    def _graceful_shutdown(self, signum=None, frame=None):
        logger.debug(f'Got signal {signum}, frame {frame}')
        logger.info('Stopped RPC server, Waiting for RPCs to complete...')
        self.server.stop(30)
        logger.info('Server stopped')
        self._stop_event.set()
