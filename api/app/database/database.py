from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import functools


db = SQLAlchemy()
migrate = Migrate()

def session(func):
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        try:
            session = db.session()
            response = func(*args, **kwargs, session=session)
            session.commit()
            return response
        except:
            session.rollback()
    return wraps
