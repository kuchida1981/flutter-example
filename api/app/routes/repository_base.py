from app.database import Session


class RepositoryBase:

    def __init__(self, session: Session):
        self._session = session
