import random

from catboost import CatBoostRegressor # type: ignore[import-untyped]

from app.storage.unit_of_work import UnitOfWork
from app.schemas import CampaignParameters, CampaignRegions
from app.models.plan import IParticleSwarmOptimization

class CampaignService:
    @staticmethod
    def plan_campaign(uow: UnitOfWork, assess_model: IParticleSwarmOptimization, parameters: CampaignParameters) -> CampaignRegions:
        return CampaignRegions([random.randint(0, 150) for _ in range(9)])
    
    @staticmethod
    def assess_campaign(uow: UnitOfWork, model: CatBoostRegressor, regions: CampaignRegions) -> float:
        return 0.0 

