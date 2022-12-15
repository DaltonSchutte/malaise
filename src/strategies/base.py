"""
Base class for strategies
"""
from typing import (Union)

from ..orders import (Order,
                      ORDER_TYPES
                     )

###########
# CLASSES #
###########

class BaseStrategy:
    def __init__(self):
        pass

    def load(self,
             config_path:str
            ):
        pass

    def execute_orders(self,
                       orders:str=None
                      ):
        """
        Attempts to place provided trades

        TODO:
            accept orders as:
                iterable of Order
                dict{'symbol':float} (neg->sell, pos->buy)
        """
        pass
