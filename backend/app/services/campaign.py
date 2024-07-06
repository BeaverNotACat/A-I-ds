import random

from tensorflow import Module  # type: ignore[import-untyped]

from app.storage.unit_of_work import UnitOfWork
from app.schemas import CampaignParameters, CampaignRegions

class CampaignService:
    @staticmethod
    def plan_campaign(uow: UnitOfWork, model: Module, parameters: CampaignParameters) -> CampaignRegions:
        return CampaignRegions([random.randint(0, 150) for _ in range(9)])
    
    @staticmethod
    def assess_campaign(uow: UnitOfWork, model: Module, regions: CampaignRegions) -> float:
        return 0.0 

