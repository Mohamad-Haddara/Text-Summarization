from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema

from app.models.tortoise import SummarySchema


router = APIRouter()


# POST Router
# Define a handler that expect a payload, payload: SummaryPayloadSchema, with a URL

@router.post("/", response_model = SummaryResponseSchema, status_code = 201)
async def create_summary(payload: SummaryPayloadSchema):
    summary_id = await crud.post(payload)
    
    response_object = {
        "id": summary_id,
        "url": payload.url
    }
    
    return response_object


# Get Router
@router("/{id}/", response_model = SummarySchema)
async def read_summary(id: int) -> SummarySchema:
    summary = await crud.get(id)
    
    # If summary ID Doesn't exist
    if not summary:
        raise HTTPException(status_code = 404, detail="Summary not found")
    
    return summary