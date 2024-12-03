from fastapi.testclient import TestClient
from ..controllers import promo as controller
from ..main import app
import pytest
from ..models import promo as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_promo(db_session):
    # Create a sample promo code
    promo_data = {
        "code": "12345",
        "expiration_date": "2024-12-03"
    }

    promo_object = model.Promo(**promo_data)

    # Call the create function
    created_promo = controller.create(db_session, promo_object)

    # Assertions
    assert created_promo is not None
    assert created_promo.code == "12345"
    assert created_promo.expiration_date == "2024-12-03"
