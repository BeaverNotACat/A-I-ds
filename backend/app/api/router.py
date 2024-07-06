from litestar import Router, post
from catboost import CatBoostRegressor # type: ignore[import-untyped]

from app.services.campaign import CampaignService
from app.schemas import CampaignParameters, CampaignRegions
from app.storage.unit_of_work import UnitOfWork
from app.models.plan import IParticleSwarmOptimization


@post(
    path="/assess",
)
async def assess_campaign(uow: UnitOfWork, assess_model: CatBoostRegressor, data: CampaignRegions) -> float:
    async with uow:
        return CampaignService.assess_campaign(uow, assess_model, data)


@post(
    path="/plan",
)
async def plan_campaign(
    uow: UnitOfWork, plan_model: IParticleSwarmOptimization, data: CampaignParameters
) -> CampaignRegions:
    async with uow:
        return CampaignService.plan_campaign(uow, plan_model, data)


router = Router(
    path="/",
    route_handlers=[assess_campaign, plan_campaign],
)
