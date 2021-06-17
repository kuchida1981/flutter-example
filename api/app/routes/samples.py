from fastapi import APIRouter, status, Depends, HTTPException
from app import models
from app import dependencies
from app.database import Sample
from .sample_repository import SampleRepository


router = APIRouter(
    prefix="/samples"
)


@router.get(
    "",
    summary="Sample collection",
    description="Sample collection",
    response_model=models.SampleList,
)
async def list_item(session=Depends(dependencies.db_session)):
    return SampleRepository(session).list_item()


@router.get(
    "/{item_id}",
    response_model=models.Sample,
)
async def get(item_id: int, session=Depends(dependencies.db_session)):
    if (sample := SampleRepository(session).get_item(item_id)) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return sample


@router.post(
    "",
    summary="Post Sample",
    description="Sample list",
    status_code=status.HTTP_201_CREATED,
    response_model=models.Sample,
)
async def post(sample: models.SampleIn, session=Depends(dependencies.db_session)):
    return SampleRepository(session).create(sample)
