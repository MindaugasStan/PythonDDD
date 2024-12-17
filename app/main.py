from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request

from app.company.routes import company_router
from app.employee.routes import employee_router
from app.seniority_level.routes import level_router

app = FastAPI(title="Employee service")
app.include_router(employee_router)
app.include_router(company_router)
app.include_router(level_router)


@app.exception_handler(Exception)
async def validation_exception_handler(request: Request, exc: Exception):
    # Change here to Logger
    return JSONResponse(
        status_code=500,
        content={
            "message": (
                f"Failed method {request.method} at URL {request.url}."
                f" {exc!r}."
            )
        },
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}
