from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str

@app.post("/calculate")
def calculate(request: CalculationRequest):
    num1 = request.num1
    num2 = request.num2
    operation = request.operation

    if operation not in ["add", "subtract", "multiply", "divide"]:
        raise HTTPException(status_code=400, detail="Invalid operation. Choose 'add', 'subtract', 'multiply', or 'divide'.")

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero.")
        result = num1 / num2

    return {"result": result}