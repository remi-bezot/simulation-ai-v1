from fastapi import FastAPI
from app.routers import agents_router, multiverse_router

app = FastAPI(title="Simulation AI v3")

app.include_router(agents_router.router, prefix="/api/agents")
app.include_router(multiverse_router.router, prefix="/api/multiverse")


@app.get("/")
def root():
    return {"message": "Bienvenue dans Simulation AI v3!"}
