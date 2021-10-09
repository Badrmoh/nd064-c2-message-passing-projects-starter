import grpc
import location_pb2
import location_pb2_grpc
import logging
import time
from concurrent import futures
from services import LocationService
from google.protobuf.json_format import MessageToJson
from utils.database import DB
from utils.producer import Kafka
from utils.configs import MAX_WORKERS, SERVER_PORT


# Definition of protobuf services 
class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        location_json = MessageToJson(request)
        # Make sure that Kafka is connected.
        producer = Kafka()
        producer.publish(message=location_json)
        return request

    def Retrieve(self, request, context):
        result = LocationService.retrieve(request.location_id)
        return location_pb2.Location(**result)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # Initialize Kafka Producer
    producer = Kafka()
    
    # Initialize DB connection
    db_conn = DB()

    # Initialize gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)
    logger.debug("Server starting on port " + SERVER_PORT + " ...")
    server.add_insecure_port(SERVER_PORT)
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)