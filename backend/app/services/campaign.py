import random

from kan import KAN, torch
import numpy as np
from torch import tensor

from app.storage.unit_of_work import UnitOfWork
from app.schemas import CampaignParameters, CampaignRegions
from app.models.plan import IParticleSwarmOptimization


class CampaignService:
    @staticmethod
    def plan_campaign(
        uow: UnitOfWork,
        plan_model: IParticleSwarmOptimization,
        parameters: CampaignParameters,
    ) -> CampaignRegions:
        a = plan_model.predict(parameters.avaliable_banners)
        return CampaignRegions(regions=a[0], score=a[1])

    @staticmethod
    def assess_campaign(
        uow: UnitOfWork, assess_model: KAN, regions: list[int]
    ) -> float:
        t = tensor(np.concatenate([np.array(regions), np.array([0])]).reshape(1, -1))
        output = assess_model(t)
        return output.tolist()[0][0]
