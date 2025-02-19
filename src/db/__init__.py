from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
# from dotenv import load_dotenv

client = MongoClient('mongodb://localhost:27017/')
collection = client['portflio']['users']
class DBHelper:
    _instance =None

    async_io_db_client: AsyncIOMotorClient = None
    async_io_db_instance = None
    db_client: MongoClient = None
    db_instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super.__new__(cls)
        return cls._instance
    

    def __init__(self):
        self.async_io_db_client = AsyncIOMotorClient('mongodb://localhost:27017/')
        self.async_io_db_instance  = AsyncIOMotorClient('Portflio')
        self.db_client = MongoClient('mongodb://localhost:27017/')
        self.db_instance = MongoClient('Portflio')
        pass

class BaseDbHepler:
    def __init__(self):
        self.dbc = DBHelper()



