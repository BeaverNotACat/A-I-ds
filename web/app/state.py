from contextlib import asynccontextmanager
from typing import AsyncGenerator

from litestar import Litestar
import tensorflow as tf  # type: ignore[import-untyped]

from app.storage.unit_of_work import UnitOfWork


@asynccontextmanager
async def model_setup(app: Litestar) -> AsyncGenerator[None, None]:
    model = getattr(app.state, "model", None)
    if model is None:
        model = tf.Module()
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
