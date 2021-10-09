from utils.database import DB
import logging
from utils.producer import Kafka

k = Kafka()
print(k)
k.publish(message='1234')
print(k.conn_count)

kk = Kafka()
print(kk)
kk.publish(message='1234')
print(kk.conn_count)

# logging.basicConfig(level=logging.DEBUG)
# d = DB()

# q = 'SELECT * FROM location where id=55 LIMIT 1'
# res = d.execute(q)
# cor = res[2]

# q = 'SELECT ST_AsText(\'' + cor + '\')'
# res = d.execute(q)
# wkt_shape = res[0]
# longitude = wkt_shape[wkt_shape.find(" ") + 1 : wkt_shape.find(")")]
# latitude = wkt_shape[wkt_shape.find("(") + 1 : wkt_shape.find(" ")]
# print(wkt_shape)
# print(longitude)
# print(latitude)