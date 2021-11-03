""" Classes used to create structured bodies"""

from pydantic import BaseModel


class Item(BaseModel):
    """
    Item received from API
    contains an image of type string
    """

    image: str
