# Mongo db for text filters

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from Mizuharabot import MONGO_DB_URI

MONGO = MONGO_DB_URI

mongo_client = MongoClient(MONGO)
db = mongo_client.Mizuharabot
