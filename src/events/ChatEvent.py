from datetime import datetime
from events.event import Event


class ChatEvent(Event):
  user: str
  message: str
  datetime: datetime

  def __init__(self, jsonStr):
    self.__dict__ = jsonStr