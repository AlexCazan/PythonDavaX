# app/routers/math_router.py

from typing import Annotated
from fastapi import APIRouter, HTTPException, Path
from pydantic import BaseModel, Field

from f import MathService  # adjust import if you move f.py into a package

router = APIRouter(prefix="/math", tags=["math"])


# --- Request schemas -------------------------------------------------------

class PowBody(BaseModel):
    base: float = Field(..., example=2)
    exponent: float = Field(..., example=8)


# --- Parameter types via Annotated + Path ----------------------------------

# Fibonacci index:  0 ≤ n ≤ 10 000
FibPath = Annotated[
    int,
    Path(
        ...,
        ge=0,
        le=10_000,
        description="Index n (0 ≤ n ≤ 10 000)",
    ),
]

# Factorial input: 0 ≤ n ≤ 100 000
FactPath = Annotated[
    int,
    Path(
        ...,
        ge=0,
        le=100_000,
        description="n for factorial (0 ≤ n ≤ 100 000)",
    ),
]


# --- Endpoints --------------------------------------------------------------

@router.post(
    "/pow",
    summary="Compute base^exponent",
    response_model=dict[str, float],
)
def calculate_pow(body: PowBody):
    try:
        result = MathService.execute("pow", base=body.base, exp=body.exponent)
    except ValueError as e:
        # invalid base/exponent combination
        raise HTTPException(status_code=400, detail=str(e))
    return {"result": result}


@router.get(
    "/fib/{n}",
    summary="Get nᵗʰ Fibonacci number",
    response_model=dict[str, int],
)
def get_fib(n: FibPath):
    try:
        result = MathService.execute("fib", n=n)
    except ValueError as e:
        # e.g. negative n
        raise HTTPException(status_code=400, detail=str(e))
    return {"result": result}


@router.get(
    "/fact/{n}",
    summary="Get n! (factorial)",
    response_model=dict[str, int],
)
def get_fact(n: FactPath):
    try:
        result = MathService.execute("factorial", n=n)
    except ValueError as e:
        # e.g. n too large
        raise HTTPException(status_code=400, detail=str(e))
    return {"result": result}
