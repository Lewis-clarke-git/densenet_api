""" This route is for image predictions using a DenseNet """

from fastapi import APIRouter
from keras.applications.densenet import decode_predictions

from ..model.model import create_densenet
from ..model.preprocessing import preprocess
from ..schemas import Item

router = APIRouter(prefix="/predict", tags=["predict"])
model = create_densenet()


@router.post("", tags=["predict"])
async def process_model_prediction(item: Item):
    """
    Process the models prediction
    This function takes the APIs image, preprocesses it,
    passes it to the model, and then returns that prediction.
    """
    processed_img = preprocess(item)
    predictions = model.predict(processed_img)
    decoded_predictions = decode_predictions(predictions, top=1)
    _, prediction_string, _ = decoded_predictions[0][0]
    return {"response": prediction_string}
