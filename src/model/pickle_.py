import os
import pickle
from abc import ABCMeta, abstractmethod

class Pickle_(metaclass=ABCMeta):

    def __init__(self,path_):
        pass

    @abstractmethod
    def save_model(self):
        """This takes the path variable and saves the model."""

    @abstractmethod
    def load_model(self):
        """loads the appropriate model."""

    @abstractmethod
    def remove_model(self):
        """removes the saved_model"""