from fastapi import FastAPI

import animal_endpoints
from database import engine
import models

# fastapi config
app = FastAPI(title="FastAPI-Meetup")
app.include_router(animal_endpoints.router)

# create the database on startup
models.Base.metadata.create_all(bind=engine)


# redirect default urls to docs
# def api_docs_redirect() -> Response:
#     return RedirectResponse(url="/docs")
# app.get("")(api_docs_redirect)
# app.get("/", include_in_schema=False)(api_docs_redirect)
