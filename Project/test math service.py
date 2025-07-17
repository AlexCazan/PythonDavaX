#test math service
import math
import pytest
from f import Calculator, MathService
#from app.services.simple_math import MathService

def test_pow():
    assert MathService.execute("pow", base=2, exp=3) == 8

def test_fib():
    assert MathService.execute("fib", n=7) == 13

def test_factorial():
    assert MathService.execute("factorial", n=5) == 120


from f import Calculator  

print(Calculator.pow(2, 3))        # → 8.0
print(Calculator.fib(7))           # → 13
print(Calculator.factorial(5))     # → 120
