from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.dependencies import oauth2_scheme

subapp = FastAPI()
origins = [ # TODO: UPDATE WITH ACTUAL URL
    "http://127.0.0.1:8000",
    "https://127.0.0.1:8000"
]
subapp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@subapp.post("/create-team")
def create_team(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
