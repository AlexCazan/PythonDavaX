from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from config.swagger_config import swagger_openapi
from api.math_router import router as math_router
from pathlib import Path

app = FastAPI()
app.openapi = swagger_openapi(app)

from repository.db_repository import init_db

# Initialize database tables
init_db()


static_dir = Path(__file__).parent / "static"
app.mount("/ui", StaticFiles(directory=static_dir, html=True), name="ui")

# Redirect root to Swagger UI


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/ui")


# include your math routes
app.include_router(math_router)
