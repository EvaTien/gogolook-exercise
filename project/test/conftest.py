import pytest


from app import app
from database import engine, db_session
from models import Base


@pytest.fixture()
def client():
    app.testing = True
    with app.test_client() as client:
        with app.app_context():
            Base.metadata.create_all(bind=engine)
        yield client
    db_session.remove()
    Base.metadata.drop_all(bind=engine)
