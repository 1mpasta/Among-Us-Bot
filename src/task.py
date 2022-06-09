from abc import ABC, abstractmethod


class Task(ABC):

    @abstractmethod
    def do_task(self):
        pass

    @abstractmethod
    def check_task(self, screenshot):
        pass
