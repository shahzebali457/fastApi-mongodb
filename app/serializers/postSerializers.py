from app.serializers.userSerializers import embeddedUserResponse


def postEntity(post) -> dict:
    return {
        "id": str(post["_id"]),
        "name": post["name"],
        "age": post["age"]
    }


def populatedPostEntity(post) -> dict:
    return {
        "id": str(post["_id"]),
        "name": post["name"],
        "age": post["age"]
    }


def postListEntity(posts) -> list:
    return [populatedPostEntity(post) for post in posts]

