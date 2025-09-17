from fastapi import FastAPI
from fastapi.responses import JSONResponse


def create_app() -> FastAPI:
    app = FastAPI(title="ECHO Backend", version="0.1.0")

    @app.get("/health", tags=["health"])  # Simple health endpoint for readiness/liveness
    async def health() -> JSONResponse:
        return JSONResponse({"status": "ok"})

    @app.get("/", tags=["meta"])  # Root endpoint with minimal info
    async def root() -> JSONResponse:
        return JSONResponse({
            "name": "ECHO Backend",
            "description": "Emergency Child Homing Operations API",
            "health": "/health",
        })

    return app


app = create_app()


