from contextlib import asynccontextmanager
from typing import AsyncGenerator

from litestar import Litestar
from kan import KAN

from app.storage.unit_of_work import UnitOfWork
from app.models.plan import ParticleSwarmOptimization 


@asynccontextmanager
async def assess_model_setup(app: Litestar) -> AsyncGenerator[None, None]:
    model = getattr(app.state, "assess_model", None)
    if model is None:
        model = KAN(width=[21,51,1], grid=5, k=3, seed=0)
        model.load_ckpt('weights')
        app.state.assess_model = model
    try:
        yield
    finally:
        ...


@asynccontextmanager
async def plan_model_setup(app: Litestar) -> AsyncGenerator[None, None]:
    model = getattr(app.state, "plan_model", None)
    if model is None:
        amodel = KAN(width=[21,51,1], grid=5, k=3, seed=0)
        amodel.load_ckpt('weights')
        
        model = ParticleSwarmOptimization(amodel)
        app.state.plan_model = model
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
