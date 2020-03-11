import os
from abc import ABCMeta, abstractmethod

class Predict(metaclass=ABCMeta):
    """Base predictor to be used for all models."""

    def __init__(self, directory):
        self.directory = directory
        self.model_directory = os.path.join(directory, 'models')

    @abstractmethod
    def load_model(self):
        """Load model h
ere."""

    @abstractmethod
    def preprocess(self):
        """This takes the raw data and returns clean data for prediction."""

    @abstractmethod
    def predict(self):
        """This is used for prediction."""