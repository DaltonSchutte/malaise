"""
Class to hold market data
"""

from typing import Callable
from time import time

from pandas import DataFrame


###########
# CLASSES #
###########

class Market:
    def __init__(self):
        pass

    def fetch_update(self,
                     online:bool=False
                    ):
        pass

    def apply_strategy(self,
                       strategy:Callable
                      ):
        pass

    def save(self,
             path:str
            ):
        pass

    def plot(self):
        pass

    def __call__(self,
                 **kwargs
                ):
        self.apply_strategy(**kwargs)
