from litestar import Litestar
from litestar.di import Provide

from app.state import unit_of_work_setup, assess_model_setup, plan_model_setup
from app.utils.dependencies import unit_of_work_dependencie, assess_model_dependencie, plan_model_dependencie
from app.api.router import router

app = Litestar(
    lifespan=[assess_model_setup, plan_model_setup, unit_of_work_setup],
    dependencies = {
        "uow": Provide(unit_of_work_dependencie),
        "assess_model": Provide(assess_model_dependencie),
        "plan_model": Provide(plan_model_dependencie)
    },
    route_handlers=[router]
)
