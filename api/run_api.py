import uvicorn
from fastapi import FastAPI
from routers.home import get_home
from constants import DB_DATABASE
from routers.v_1 import get_product_info, get_categories_info, get_product_category_info

app_api = FastAPI()
v_1_0 = FastAPI()


@app_api.on_event("startup")
async def startup():
    await DB_DATABASE.connect()


@app_api.on_event("shutdown")
async def shutdown():
    await DB_DATABASE.disconnect()


app_api.include_router(get_home.router)

# router api v1.0
v_1_0.include_router(get_product_info.router)
v_1_0.include_router(get_categories_info.router)
v_1_0.include_router(get_product_category_info.router)
app_api.mount("/api/v1.0", v_1_0)

if __name__ == "__main__":
    uvicorn.run(app_api, host="0.0.0.0", port=8090)
