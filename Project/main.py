from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import inspect
from api.math_router import router as math_router
from pathlib import Path
from repository.db_repository import init_db, engine

app = FastAPI()

# Initialize database tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    insp = inspect(engine)
    if not insp.has_table("math_requests"):
        init_db()
    yield

static_dir = Path(__file__).parent / "static"
app.mount("/ui", StaticFiles(directory=static_dir, html=True), name="ui")

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/ui")

# include your math routes
app.include_router(math_router)
