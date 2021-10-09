import logging
from utils.database import DB

logger = logging.getLogger(__name__)


class LocationService:
    @staticmethod
    def retrieve(location_id):
        logger.debug('Retrieving location for id ' + location_id)
        db_conn = DB()
        LOCATION_QUERY = str('SELECT id,person_id,coordinate,creation_time'
                              + ' FROM location where id='
                              + str(location_id) + ' LIMIT 1')
        LOCATION = db_conn.execute(LOCATION_QUERY)
        if not LOCATION:
            return
        WKT_QUERY = 'SELECT ST_AsText(\'' + LOCATION[2] + '\')'
        WKT_SHAPE = db_conn.execute(WKT_QUERY)[0]

        LOCATION_ID = LOCATION[0]
        PERSON_ID = LOCATION[1]
        LONGITUDE = WKT_SHAPE[WKT_SHAPE.find(" ") + 1: WKT_SHAPE.find(")")]
        LATITUDE = WKT_SHAPE[WKT_SHAPE.find("(") + 1: WKT_SHAPE.find(" ")]
        CREATION_TIME = LOCATION[3]

        result = {
            "id": str(LOCATION_ID),
            "person_id": str(PERSON_ID),
            "longitude": str(LONGITUDE),
            "latitude": str(LATITUDE),
            "creation_time": str(CREATION_TIME),
        }

        return result
