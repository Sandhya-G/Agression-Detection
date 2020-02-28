import os
from abc import ABCMeta, abstractmethod

class Trainer(metaclass=ABCMeta):
    """Base trainer to be used for all models."""

    def __init__(self, directory):
        self.directory = directory
        self.model_directory = os.path.join(directory, 'models')

    @abstractmethod
    def preprocess(self):
        """This takes the preprocessed data and returns clean data. This is more about statistical or text cleaning."""

    @abstractmethod
    def set_model(self):
        """Define model here."""

    @abstractmethod
    def fit_model(self):
        """This takes the vectorised data and returns a trained model."""

    @abstractmethod
    def generate_metrics(self):
        """Generates metric with trained model and test data."""

    @abstractmethod
    def save_model(self, model_name):
        """This method saves the model in our required format."""

