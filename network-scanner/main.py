# Imports
from contextlib import asynccontextmanager # Used to control session such as starting and closing it

# Fastapi usage
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Local imports
from network-scanner.operations.database.core import Base, SessionMaker, engine
from network-scanner.operations.routes import Admin, Product


# Async usage to manage a session
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    yield

app = FastAPI(lifespan=lifespan)