from pydantic import BaseModel




class SummaryPayloadSchema(BaseModel):
    url: str
    

# SummaryResponseSchema inherits from SummaryPayloadSchema model, adding id field
class SummaryResponseSchema(SummaryPayloadSchema):
    id: int
    
