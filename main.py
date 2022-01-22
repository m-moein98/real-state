from fastapi import FastAPI

from authentication_app.views import api_router as auth_router
from listing_app.views import api_router as listing_router



app = FastAPI()
app.include_router(auth_router, prefix="")
app.include_router(listing_router, prefix="/api/listing")
