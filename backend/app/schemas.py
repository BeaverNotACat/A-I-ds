import re
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, RootModel, field_validator, ValidationInfo


class Gender(StrEnum):
    ALL = "all"
    MALE = "male"
    FEMALE = "female"


class CampaignParameters(BaseModel):
    """
    Represents model intput parameters
    """

    model_config = ConfigDict(from_attributes=True)
    gender: Gender
    age_from: int
    age_to: int
    income: str
    avaliable_banners: int

    @field_validator("income")
    @classmethod
    def validate_income(cls, income: str, info: ValidationInfo):
        assert (
            re.fullmatch("^[a-c]*", income) is not None
        ), f"{info.field_name} must be ^[a-c]*"  # TODO Make better validation
        return income


class CampaignRegions(BaseModel):  # TODO make more human-redable representation schema
    """
    Represents model output: vector of map sectors with required banners amount
    """

    model_config = ConfigDict(from_attributes=True)
    regions: list[int]
    score: float
