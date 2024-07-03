from litestar import Router, get
from litestar.contrib.htmx.request import HTMXRequest
from litestar.contrib.htmx.response import HTMXTemplate
from litestar.response import Template

from tensorflow import Module  # type: ignore[import-untyped]

from app.storage.unit_of_work import UnitOfWork


@get(
    path="/example",
)
def example(request: HTMXRequest, uow: UnitOfWork, model: Module) -> Template:
    return HTMXTemplate(template_name="main.html")


example_router = Router(
    path="/",
    route_handlers=[example],
)
