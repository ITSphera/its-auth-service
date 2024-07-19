import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.settings import server_settings
from fastapi.openapi.utils import get_openapi

from api.v1.routers import all_routers_v1

app = FastAPI(
    # openapi_url=database_settings.openapi_url,
    # swagger_ui_init_oauth={
    #     "clientId": database_settings.client_id,
    #     "clientSecret": database_settings.client_secret,
    # },
    # swagger_ui_parameters={"displayRequestDuration": True, "persistAuthorization": True},
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        summary="This is a very custom OpenAPI schema",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

# CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)

# Routing
for router in all_routers_v1:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=server_settings.HOST,
        port=int(server_settings.PORT),
        reload=True,
    )
