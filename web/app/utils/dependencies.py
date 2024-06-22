from litestar.datastructures import State

from app.storage.unit_of_work import UnitOfWork
from tensorflow import Module  # type: ignore[import-untyped]

async def unit_of_work_dependencie(state: State) -> UnitOfWork:
    unit_of_work = getattr(state, "unit_of_work", None)
    if unit_of_work is None:
        raise ValueError("Unit of work is not in state")
    return unit_of_work


async def model_dependencie(state: State) -> Module:
    model = getattr(state, "model", None)
    if model is None:
        raise ValueError("Model is not in state")
    return model
