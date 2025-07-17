from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from config.swagger_config import swagger_openapi
from api.math_router import router as math_router   

app = FastAPI()
app.openapi = swagger_openapi(app)

# Redirect root to Swagger UI
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

app.include_router(math_router)