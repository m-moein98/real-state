def user_serilaizer(user) -> dict:
    return {
        "_id": str(user["_id"]),
        "username": user["username"],
        "fullName": user["fullName"],
        "email": user["email"],
        "password": user["password"],
        "DoB": user["DoB"],
        "gender": user["gender"],
        "createdAt": user["createdAt"],
        "updatedAt": user["updatedAt"]
    }
