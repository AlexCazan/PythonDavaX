from Project.repository.db_repository import MathRequest, SessionLocal
from .calculator import Calculator

class MathService:
    """
    Micro‑façade that external layers (FastAPI, CLI, tests) can call.
    Keeps the public API narrow and allows you to swap algorithms later
    without touching the rest of the app.
    """
    _ops = {
        "pow": Calculator.pow,
        "fib": Calculator.fib,
        "factorial": Calculator.factorial,
    }

    @classmethod
    def execute(cls, op: str, **params):
        try:
            func = cls._ops[op]
        except KeyError as exc:
            raise ValueError(f"Unknown operation '{op}'") from exc
        return func(**params)

 # Persist the request
        cls._save_to_db(op, params, result)

        return result

    @staticmethod
    def _save_to_db(op: str, params: dict, result: float):
        session = SessionLocal()
        try:
            entry = MathRequest(
                operation=op,
                parameters=str(params),
                result=result,
            )
            session.add(entry)
            session.commit()
        finally:
            session.close()