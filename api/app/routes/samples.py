from fastapi import APIRouter, Depends, HTTPException, status

from app import models

from app.repositories import SampleRepository

router = APIRouter(
    prefix="/samples"
)


@router.get(
    "",
    summary="Sample collection",
    description="Sample collection",
    response_model=models.SampleList,
)
async def list_item(repository=Depends(SampleRepository)):
    return repository.list_item()


@router.get(
    "/{item_id}",
    response_model=models.Sample,
)
async def get(item_id: int, repository=Depends(SampleRepository)):
    if (sample := repository.get_item(item_id)) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return sample


@router.post(
    "",
    summary="Post Sample",
    description="Post Sample",
    status_code=status.HTTP_201_CREATED,
    response_model=models.Sample,
)
async def post(sample: models.SampleIn, repository=Depends(SampleRepository)):
    return repository.create(sample)
