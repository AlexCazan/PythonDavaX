from fastapi.openapi.utils import get_openapi


def swagger_openapi(app):
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="HomeworkPython API",
            version="1.0.0",
            description="This is a custom OpenAPI",
            routes=app.routes,
        )
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    return custom_openapi
