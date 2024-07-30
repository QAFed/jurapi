import pytest
from endpoints.clear_db import ClearDB


@pytest.fixture
def pre_clear():
    clear_db = ClearDB()
    clear_db.clear_db()
    yield
    clear_db.clear_db()
