from contextlib import asynccontextmanager
from typing import AsyncGenerator

from litestar import Litestar
from catboost import CatBoostRegressor # type: ignore[import-untyped]

from app.storage.unit_of_work import UnitOfWork
from app.models.plan import ParticleSwarmOptimization 


@asynccontextmanager
async def assess_model_setup(app: Litestar) -> AsyncGenerator[None, None]:
    model = getattr(app.state, "assess_model", None)
    if model is None:
        model = CatBoostRegressor().load_model("../assess_model_weigts")
        app.state.model = model
    try:
        yield
    finally:
        ...


@asynccontextmanager
async def plan_model_setup(app: Litestar) -> AsyncGenerator[None, None]:
    model = getattr(app.state, "plan_model", None)
    if model is None:
        model = ParticleSwarmOptimization(getattr(app.state, "assess_model"))
        app.state.model = model
    try:
        yield
    finally:
        ...


@asynccontextmanager
async def unit_of_work_setup(app: Litestar) -> AsyncGenerator[None, None]:
    unit_of_work = getattr(app.state, "unit_of_work", None)
    if unit_of_work is None:
        unit_of_work = UnitOfWork()
        app.state.unit_of_work = unit_of_work
    try:
        yield
    finally:
        pass
