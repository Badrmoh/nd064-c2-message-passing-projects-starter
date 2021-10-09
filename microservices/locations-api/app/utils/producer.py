import logging
import json
from kafka import KafkaProducer, errors
from utils.configs import KAFKA_SERVICE, KAFKA_TOPIC

logger = logging.getLogger(__name__)


class Kafka(object):
    # A Singletone class
    conn = None
    conn_count = 0

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Kafka.__instance:
            Kafka.__instance = object.__new__(cls)
        return Kafka.__instance

    def __init__(self):
        if Kafka.conn is None:
            try:
                Kafka.conn = KafkaProducer(
                    bootstrap_servers=KAFKA_SERVICE,
                    value_serializer=lambda m: json.dumps(m).encode('utf-8'),
                    retries=5)
                Kafka.conn_count += 1
            except Exception:
                logger.error("... Kafka is not available ...")
            except errors.KafkaTimeoutError as err:
                logger.error(err)


    @classmethod
    def success(b, record_metadata):
        logger.debug("Meta: " + str(record_metadata))
        logger.debug("TOPIC: " + str(record_metadata.topic))
        logger.debug("OFFSET: " + str(record_metadata.offset))


    @classmethod
    def error(err):
        logger.error('Kafka error: ', exc_info=err)


    @classmethod
    def publish(self, message):
        Kafka.conn.send(KAFKA_TOPIC, message).add_callback(self.success).add_errback(self.error)
        Kafka.conn.flush()
