from litestar import Router, get
from litestar.response import Template

from tensorflow import Module  # type: ignore[import-untyped]

from app.storage.unit_of_work import UnitOfWork


@get(
    path="/example",
)
def example(uow: UnitOfWork, model: Module) -> str:
    return "Hello, world!"


example_router = Router(
    path="/",
    route_handlers=[example],
)
