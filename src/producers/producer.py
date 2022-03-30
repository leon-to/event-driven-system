from abc import ABC, abstractmethod

class Producer(ABC):
  @abstractmethod
  def produce(self, event):
    pass