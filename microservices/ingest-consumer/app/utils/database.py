import psycopg2
import logging
from utils.configs import DB_PASSWORD, DB_USERNAME, DB_PORT, DB_HOST, DB_NAME

logger = logging.getLogger(__name__)


class DB(object):
    # A Singletone class
    conn = None
    conn_count = 0

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not DB.__instance:
            DB.__instance = object.__new__(cls)
        return DB.__instance


    def __init__(self):
        if DB.conn is None:
            try:
                # connect to the PostgreSQL server
                logger.debug('Connecting to the database...')
                DB.conn = psycopg2.connect(
                    host=DB_HOST,
                    user=DB_USERNAME,
                    port=DB_PORT,
                    database=DB_NAME,
                    password=DB_PASSWORD)
                DB.conn_count += 1
            except (Exception, psycopg2.DatabaseError) as error:
                logger.error(error)


    @staticmethod
    def execute(query):
        logger.debug('Querying the database...')
        cur = DB.conn.cursor()
        try:
            cur.execute(query)
            cur.close()
        except Exception as err:
            cur.execute("ROLLBACK")
            logger.error(err)

