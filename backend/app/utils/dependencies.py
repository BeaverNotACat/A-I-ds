from litestar.datastructures import State

from app.storage.unit_of_work import UnitOfWork
from catboost import CatBoostRegressor # type: ignore[import-untyped]


async def unit_of_work_dependencie(state: State) -> UnitOfWork:
    unit_of_work = getattr(state, "unit_of_work", None)
    if unit_of_work is None:
        raise ValueError("Unit of work is not in state")
    return unit_of_work


async def assess_model_dependencie(state: State) -> CatBoostRegressor:
    model = getattr(state, "assess_model", None)
    if model is None:
        raise ValueError("Assess model is not in state")
    return model


async def plan_model_dependencie(state: State):
    model = getattr(state, "plan_model", None)
    if model is None:
        raise ValueError("Plan model is not in state")
    return model
