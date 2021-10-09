import grpc
import location_pb2
import location_pb2_grpc
import datetime
from os import environ

SERVER = str(environ.get('SERVER', 'localhost:5005'))

channel = grpc.insecure_channel(SERVER)
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.Location(
    longitude='-105.5719566',
    latitude='35.0585126',
    person_id='9',
)
location_id = location_pb2.LocationID(location_id=str('55'))
response = stub.Retrieve(location_id)
response = stub.Create(location)
print(response)