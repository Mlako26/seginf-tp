from abc import ABC, abstractmethod

class HoneyTokenGenerator(ABC):
    @abstractmethod
    def generate(self, output_path: str, enpoint_base_uri: str, **kwargs):
        pass
