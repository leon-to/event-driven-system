from datetime import datetime
from cores.core import Core
from events.ChatEvent import ChatEvent

# set now datetime to chat event
class ChatCore(Core):
  def engage(self, event: ChatEvent) -> ChatEvent:
    event.datetime = datetime.now()
    return event