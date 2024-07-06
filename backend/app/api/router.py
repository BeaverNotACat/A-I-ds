from litestar import Router, post

from tensorflow import Module  # type: ignore[import-untyped]

from app.services.campaign import CampaignService
from app.schemas import CampaignParameters, CampaignRegions
from app.storage.unit_of_work import UnitOfWork


@post(
    path="/assess",
)
async def assess_campaign(uow: UnitOfWork, model: Module, data: CampaignRegions) -> float:
    async with uow:
        return CampaignService.assess_campaign(uow, model, data)


@post(
    path="/plan",
)
async def plan_campaign(
    uow: UnitOfWork, model: Module, data: CampaignParameters
) -> CampaignRegions:
    async with uow:
        return CampaignService.plan_campaign(uow, model, data)


router = Router(
    path="/",
    route_handlers=[assess_campaign, plan_campaign],
)
