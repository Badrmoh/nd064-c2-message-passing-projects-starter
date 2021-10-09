import logging
import json
from kafka import KafkaConsumer, errors
from utils.configs import KAFKA_HOST_STRING, KAFKA_TOPIC


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
                Kafka.conn = KafkaConsumer(KAFKA_TOPIC,
                        value_deserializer=lambda m:
                        json.loads(m.decode('utf-8')),
                        bootstrap_servers=KAFKA_HOST_STRING)
                Kafka.conn_count += 1
            except Exception:
                logger.error("... Kafka is not available ...")
            except errors.KafkaTimeoutError as err:
                logger.error(err)

    
    @classmethod
    def fetch(self):
        msgs = Kafka.conn.poll(timeout_ms=500, max_records=1)
        for tp, messages in msgs.items():
            for message in messages:
                return message.value