from glob import glob
import json
import os
from textwrap import indent
from consumers.consumer import Consumer

class JsonFileConsumer(Consumer):
  def __init__(self, path: str):
    self.path = path

  def consume(self):
    events = []
    for json_file in glob(f'{self.path}/*'):
      with open(json_file, 'r') as f:
        events.append(json.load(f))
    return events
