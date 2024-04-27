import uvicorn
from fastapi import FastAPI
from database import SessionLocal, engine, base
from routers import user as UserRouter
from fastapi.middleware.cors import CORSMiddleware

base.metadata.create_all(bind=engine)

app = FastAPI()

origins = "*"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserRouter.router, prefix="/user")

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=1407, reload=True, workers=3)
