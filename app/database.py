# import pymongo
# from pymongo import mongo_client

import motor
from bson.objectid import ObjectId
from app.config import settings
import motor.motor_asyncio
client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
print('Connected to MongoDB...')

db = client[settings.MONGO_INITDB_DATABASE]

# print(db["user"],"db.get_collection-----------------------")
users_collection = db['user']
# db.get_collection("user")


# Post = db.posts
# User.create_index([("email", pymongo.ASCENDING)], unique=True)
# Post.create_index([("title", pymongo.ASCENDING)], unique=True)

def user_helper(user) -> dict:
    return {
        "id": user["id"],
        "name": user["name"],
        # "email": user["email"],
        "age": user["age"]
    }





# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    
    user = await users_collection.find_one({"id": user_data.get('id')})

    if user:
        return None
    user = await users_collection.insert_one(user_data)
    

    new_user = await users_collection.find_one({"id": user_data.get('id')})

    return user_helper(new_user)

# Retrieve all users present in the database
async def retrieve_users():
    users = []
    async for user in users_collection.find():
        users.append(user_helper(user))
    return users

# Retrieve a user with a matching ID
async def retrieve_user(id: int) -> dict:
    user = await users_collection.find_one({"id": int(id)})
    if user:
        return user_helper(user)


# Update a user with a matching ID
async def update_user(id: int, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await users_collection.find_one({"id": int(id)})
    if user:
        updated_user = await users_collection.update_one(
            {"id": int(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


# Delete a user from the database
async def delete_user(id: str):
    user = await users_collection.find_one({"id": int(id)})
    if user:
        await users_collection.delete_one({"id": int(id)})
        return True