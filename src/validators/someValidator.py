from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from ..customs import Configs, ChangeCase
from pydantic import BaseModel, Field, Json


class Signals(BaseModel):

    pass

    # DEFINE PYDANTIC MODELS TO WORK WITH THIS
    # class Response(BaseModel):
    #     id: int
    #     instan: int
    #     closed: bool
    #     pair: str
    #     model: str
    #     entryDetails: Dict[str, Any]
    #     exitDetails: Dict[str, Any]
    #     tpHitLevel: int
    #     ads: Dict[str, Any] = None

    # class Add(BaseModel):
    #     signalId: int
    #     pair: str
    #     model: str = 'dede'
    #     entryDetails: Dict[str, Any]
    #     exitDetails: Dict[str, Any]

    # This method converts the Pydantic model to dictionary suitable for database insertion
    # def to_dict(self):
    #     # return ChangeCase.camelToSnake(self.model_dump())
    #     fieldmaps = {"signalId": "signal_id",
    #                  "entryDetails": "entry_details",
    #                  "exitDetails": "exit_details"
    #                  }
    #     return Configs.convertPyToDict(self.model_dump(), fieldmaps)
