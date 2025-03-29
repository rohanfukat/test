from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # specific frontend ka URL de sakte ho
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

class userValidation(BaseModel):
    username: str
    email: str | None = None
    password: str
    tax: float | None = None

@app.post("/user/")
def demo(user:userValidation):
    return {"Success":user}


