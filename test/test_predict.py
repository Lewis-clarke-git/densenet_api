""" API tests for the predict API """

from fastapi.testclient import TestClient
import json
from app.main import app

client = TestClient(app)
testfile = "./test/test_images/jeep.json"


def test_the_model_is_able_to_correctly_predict_an_image():
    with open(testfile, "r") as json_file:
        image = json.load(json_file)
        response = client.post("/predict", json=image)
        assert response.status_code == 200
        assert response.json() == {"response": "jeep"}


def test_the_response_if_the_image_is_missing():
    response = client.post("/predict", json={})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "image"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }


def test_the_response_if_a_bad_image_is_given():
    response = client.post("/predict", json={"image": 5})
    assert response.status_code == 400
    assert response.json() == {"detail": "Bad Image: Please use a 64b encoded image."}
