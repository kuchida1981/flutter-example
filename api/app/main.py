from fastapi import FastAPI, Response, status
from . import routes
from . import middlewares


app = FastAPI(
    title="Flutter Example API",
    description="Flutterと戯れるために用意したWeb API.",
)

middlewares.setup(app)

for route in routes.routers:
    app.include_router(route)


@app.get("/", include_in_schema=False)
async def root():
    return Response(
        status_code=status.HTTP_302_FOUND,
        headers={"Location": "/docs"},
    )
