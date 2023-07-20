from fastapi import FastAPI

import animal_endpoints

# fastapi config
app = FastAPI(title="FastAPI-Meetup")
app.include_router(animal_endpoints.router)


# redirect default urls to docs
# def api_docs_redirect() -> Response:
#     return RedirectResponse(url="/docs")
# app.get("")(api_docs_redirect)
# app.get("/", include_in_schema=False)(api_docs_redirect)
