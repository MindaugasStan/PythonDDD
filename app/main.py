from fastapi import FastAPI

from app.company.routes import company_router
from app.employee.routes import employee_router
from app.seniority_level.routes import level_router

app = FastAPI(title="Employee service")
app.include_router(employee_router)
app.include_router(company_router)
app.include_router(level_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
