
from fastapi import APIRouter, HTTPException
from app.controller.controller import *
from app.models.models import *

router = APIRouter()

@router.get("/", include_in_schema=False)
def home():
    return "Esta página está funcionando! Acesse a documentação adicionando /docs ao final da url =)"

@router.post("/add", response_model=OperationResponse, summary="Adição", description="Soma dois números.")
def add_numbers(request: OperationRequest):

    result = add(request.a, request.b)
    return OperationResponse(result=result)

@router.post("/subtract", response_model=OperationResponse, summary="Subtração", description="Subtrai dois números.")
def subtract_numbers(request: OperationRequest):

    result = subtract(request.a, request.b)
    return OperationResponse(result=result)

@router.post("/multiply", response_model=OperationResponse, summary="Multiplicação", description="Multiplica dois números.")
def multiply_numbers(request: OperationRequest):

    result = multiply(request.a, request.b)
    return OperationResponse(result=result)

@router.post("/divide", response_model=OperationResponse, summary="Divisão", description="Divide dois números.")
def divide_numbers(request: OperationRequest):

    try:
        result = divide(request.a, request.b)
        return OperationResponse(result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/sqrt", response_model=OperationResponse, summary="Raiz Quadrada", description="Raiz quadrada de um número.")
def sqrt_numbers(request: OperationRequest2):

    try:
        result = sqrt(request.a)
        return OperationResponse(result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/exponencial", response_model=OperationResponse, summary="Exponencial", description="Calcula um número elevado a outro.")
def exponent_numbers(request: OperationRequest):

    result = exponent(request.a, request.b)
    return OperationResponse(result=result)

@router.post("/factorial", response_model=OperationResponse, summary="Fatorial", description="Fatorial de um número.")
def fact_numbers(request: OperationRequest2):

    result = factorial(request.a)
    return OperationResponse(result=result)