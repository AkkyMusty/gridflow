from fastapi import FastAPI
from gridflow.routers import users, energy, trading

app = FastAPI(title="GridFlow Energy API")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(energy.router, prefix="/energy", tags=["Energy"])
app.include_router(trading.router, prefix="/trading", tags=["Trading"])

@app.get("/")
def root():
    return {"message": "Welcome to GridFlow API!"}
