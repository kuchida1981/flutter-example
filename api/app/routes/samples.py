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
async def list_item(
    page_params: models.PaginationParams = Depends(),
    repository: SampleRepository = Depends(),
):
    return repository.listitem(page_params)


@router.get(
    "/{item_id}",
    response_model=models.Sample,
)
async def get(
    item_id: int,
    repository: SampleRepository = Depends(),
):
    if (sample := repository.getitem(item_id)) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return sample


@router.post(
    "",
    summary="Post Sample",
    description="Post Sample",
    status_code=status.HTTP_201_CREATED,
    response_model=models.Sample,
)
async def post(
    sample: models.SampleIn,
    repository: SampleRepository = Depends(),
):
    return repository.create(sample)
