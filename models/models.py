from pydantic import BaseModel


class RiskAnalysis(BaseModel):
    questionId: str
    answer: str


class PersonalData(BaseModel):
    name: str


class QuickQuotationRequest(BaseModel):
    OperationCode: str
    IsPreRevamp: bool
    RiskAnalysis: list[RiskAnalysis]
    PersonalData: PersonalData
    deductibleOption: int = 2


class QuickQuotationResponse(BaseModel):
    identifier: str
    proposalNumber: str
    name: str
    status: int
    netValue: float
    discount: float
    commission: float
    commissionDiscount: float
    selectedCommission: float
    selectedPremiumIncreasePercentage: float
    premiumIncreaseValue: float
    message: str
    totalAmount: float
