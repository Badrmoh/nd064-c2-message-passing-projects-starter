import logging
from typing import Dict
from utils.database import DB

logger = logging.getLogger(__name__)


class LocationService:
    @staticmethod
    def create(request: Dict):
        
        logger.debug(str('Registering location for person_id '
                     + str(request['personId'])))

        db_conn = DB()

        COORDINATES = str(', ST_Point(' + str(request['longitude'])
                          + ', ' + str(request['latitude']) + ')')
        INSERT_QUERY = str('INSERT INTO location (person_id, coordinate) values '
                           + '(' +  str(request['personId']) + COORDINATES + ')')

        db_conn.execute(INSERT_QUERY)

