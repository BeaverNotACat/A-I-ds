from pathlib import Path

from litestar import Litestar
from litestar.di import Provide
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig

from app.state import model_setup, unit_of_work_setup
from app.utils.dependencies import unit_of_work_dependencie, model_dependencie
from app.views.example import example_router

app = Litestar(
    lifespan=[model_setup, unit_of_work_setup],
    dependencies = {
        "uow": Provide(unit_of_work_dependencie),
        "model": Provide(model_dependencie)
    },
    template_config=TemplateConfig(
        directory=Path("app/templates"),
        engine=JinjaTemplateEngine,
    ),
    route_handlers=[example_router]
)
