from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional


class EventBase(BaseModel):
    event_name: str = Field(..., description="Nom de l'événement")


class EventCreate(EventBase):
    pass


class EventLog(BaseModel):
    event_name: str
    timestamp: datetime


class EventLogResponse(BaseModel):
    events: List[EventLog] = Field([], description="Liste des événements enregistrés")
