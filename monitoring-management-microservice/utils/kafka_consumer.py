from aiokafka import AIOKafkaConsumer

from utils.logger import logger_config

from config import get_config

logger = logger_config(__name__)

configs = get_config()

def get_consumer() -> AIOKafkaConsumer:
    return AIOKafkaConsumer(
        configs["KAFKA_TOPICS"],
        bootstrap_servers=configs["KAFKA_INSTANCE"]
    )

consumer = get_consumer()

async def consume():
    while True:
        async for msg in consumer:
            payload = {
                "topic": msg["topic"],
                "partition": msg["partition"],
                "offset": msg["offset"],
                "key": msg["key"],
                "value": msg["value"],
                "timestamp": msg["timestamp"]
            }
            logger.info("Received ", str(payload))

