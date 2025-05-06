from fastapi import FastAPI
from app.views.routes import router

app = FastAPI(title="Calculadora API", description="Calculadora simples de acordo com o padrão MVC usando FastAPI")
app.include_router(router)