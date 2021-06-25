from typing import Any, List, Optional

from fastapi import Depends

from app import models
from app.database import Session
from app.dependencies import db_session


class RepositoryBase:

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def create(self, item_in: Any) -> Any:
        item = self.item_entity_class(**dict(item_in))
        self._session.add(item)
        self._session.flush()
        return item

    def listitem(self, page_params: models.PaginationParams) -> List[Any]:
        return (
            self._session.query(self.item_entity_class)
            .limit(page_params.limit)
            .offset(page_params.offset).all()
        )

    def getitem(self, item_id: int) -> Optional[Any]:
        return self._session.query(self.item_entity_class).get(item_id)
