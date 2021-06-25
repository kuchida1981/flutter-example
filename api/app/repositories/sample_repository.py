from typing import List, Optional

from app import database as db
from app import models

from .repository_base import RepositoryBase

ItemEntity = db.Sample
ItemIn = models.SampleIn


class SampleRepository(RepositoryBase):

    item_entity_class = ItemEntity

    def create(self, item_in: ItemIn) -> ItemEntity:
        return super().create_item(item_in)

    def listitem(self, page_params: models.PaginationParams) -> List[ItemEntity]:
        return super().listitem(page_params)

    def getitem(self, item_id: int) -> Optional[ItemEntity]:
        return super().getitem(item_id)
