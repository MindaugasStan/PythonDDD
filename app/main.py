from fastapi import FastAPI

from app.employee.routes import employee_router

app = FastAPI(title="Employee service")
app.include_router(employee_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
