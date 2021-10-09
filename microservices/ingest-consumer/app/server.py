import logging
import json
from time import sleep
from sys import exit
from services import LocationService
from utils.database import DB
from utils.consumer import Kafka


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # Connect to Kafka
    consumer = Kafka()

    # Initialize DB connection
    db_conn = DB()

    try:
        while True:
            # Make sure that connection to Kafka is established
            consumer = Kafka()
            if consumer is not None:
                message = consumer.fetch()
                if message is not None:
                    logger.debug(" --> Received a message!")
                    message_dict = dict(json.loads(message))
                    logger.debug(message_dict)
                    LocationService.create(message_dict)
                else:
                    logger.info("... Sleeping ...")
                    sleep(5)
    except KeyboardInterrupt:
        exit()

