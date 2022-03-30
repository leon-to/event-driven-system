from events.ChatEvent import ChatEvent
from producers.producer import Producer
from google.cloud import pubsub_v1
import os

class PubSubProducer(Producer):
  def __init__(self) -> None:
    self.publisher = pubsub_v1.PublisherClient()
    self.topic_path = self.publisher.topic_path(
      os.environ['PROJECT_ID'], 
      os.environ['TOPIC_ID'])
  
  def produce(self, event: ChatEvent):
    data = event.__dict__.__str__().encode("utf-8")
    future = self.publisher.publish(self.topic_path, data)
    return future.result()