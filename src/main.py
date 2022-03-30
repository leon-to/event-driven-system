from consumers.JsonFileConsumer import JsonFileConsumer
from cores.ChatCore import ChatCore
from events.ChatEvent import ChatEvent
from producers.PubSubProducer import PubSubProducer
from google.cloud import pubsub_v1
import os
from dotenv import load_dotenv

if __name__ == '__main__':
  load_dotenv()

  publisher = pubsub_v1.PublisherClient()
  topic_path = publisher.topic_path(os.environ['PROJECT_ID'], os.environ['TOPIC_ID'])

  consumer = JsonFileConsumer('samples')
  producer = PubSubProducer()
  core = ChatCore()
  events = consumer.consume()

  for e in events:
    event = ChatEvent(e)
    event = core.engage(event)  
    msg_id = producer.produce(event)

    print(f'Event: {event.__dict__}')
    print(f'Message ID: {msg_id}')
