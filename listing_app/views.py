from bson.objectid import ObjectId
from fastapi import APIRouter, Depends
from setting import link_collection

from .models import Createlisting, Listing
from .serializers import listing_serializer, listings_serializer
from authentication_app.auth import get_user, oauth2_scheme, token_collection, user_collection


api_router = APIRouter()


@api_router.get("/")
async def get_listing(token: str = Depends(oauth2_scheme)):
    query = link_collection.find()

    return listings_serializer(query)


@api_router.get("/{listing_id}")
async def get_listing_by_id(listing_id: str, token: str = Depends(oauth2_scheme)):
    query = link_collection.find_one({"_id": ObjectId(listing_id)})
    return listing_serializer(query)


@api_router.post("/")
async def create_listing_item(create_listing: Createlisting, token: str = Depends(oauth2_scheme)):
    user = get_user(token)
    listing = Listing(**create_listing.dict(), ownerId=str(user["_id"]))
    _id = link_collection.insert_one(dict(listing))
    instance = link_collection.find_one({"_id": _id.inserted_id})
    return listing_serializer(instance)


@api_router.put("/{listing_id}")
async def update_listing_item_by_id(listing_id: str, listing: Createlisting, token: str = Depends(oauth2_scheme)):
    link_collection.find_one_and_update(
        {"_id": ObjectId(listing_id)}, {"$set": dict(listing)})
    instance = link_collection.find_one({"_id": ObjectId(listing_id)})
    return listing_serializer(instance)


@api_router.delete("/{listing_id}")
async def delete_listing_item_by_id(listing_id: str, token: str = Depends(oauth2_scheme)):
    link_collection.find_one_and_delete({"_id": ObjectId(listing_id)})
    return {"message": "Listing item deleted"}
