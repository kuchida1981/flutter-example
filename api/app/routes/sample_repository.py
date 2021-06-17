from app.models import SampleIn
from app import database as db
from . repository_base import RepositoryBase


class SampleRepository(RepositoryBase):

    def create(self, sample_in: SampleIn):
        sample = db.Sample(**dict(sample_in))
        self._session.add(sample)
        self._session.flush()
        return sample

    def list_item(self):
        return self._session.query(db.Sample).all()

    def get_item(self, item_id: int):
        return self._session.query(db.Sample).get(item_id)
