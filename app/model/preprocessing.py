""" Preprocessing for the DenseNet Model"""

import io
import base64
from typing import Any
import numpy as np
import PIL
from keras.preprocessing import image as keras_image
from keras.applications.densenet import preprocess_input
from fastapi import HTTPException
from ..schemas import Item

target_size = (224, 224)


def preprocess(item: Item) -> Any:
    """
    Performs the preprocessing of the 64b encoded image received from
    the API ready for the DenseNet model to make predictions.
    """
    try:
        contents = base64.b64decode(item.image)
        img = PIL.Image.open(io.BytesIO(contents))
        img = img.resize(target_size)
        img_array = keras_image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

    except base64.binascii.Error:
        raise HTTPException(
            status_code=400, detail="Bad Image: Please use a 64b encoded image."
        )
        
    return img_array
