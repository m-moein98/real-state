def listing_serializer(listing_item) -> dict:
    return {
        "_id": str(listing_item["_id"]),
        "type": listing_item["type"],
        "availableNow": listing_item["availableNow"],
        "ownerId": str(listing_item["ownerId"]),
        "address": {
            "streetName": listing_item["address"]["streetName"],
            "streetNumber": listing_item["address"]["streetNumber"],
            "district": listing_item["address"]["district"],
            "city": listing_item["address"]["city"]
        },
        "createdAt": listing_item["createdAt"],
        "updatedAt": listing_item["updatedAt"]
    }


def listings_serializer(listing_items) -> list:
    return [listing_serializer(listing_item) for listing_item in listing_items]
