""" API tests for the landing page """

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """
    Checks that the server is running by checking the
    response from the landing page.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Health Test"}
