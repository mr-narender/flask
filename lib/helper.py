from lib import mongo


def db():
    return mongo.db.collection
