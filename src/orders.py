"""
Classes to handle orders
"""

from datetime import (datetime,
                      timezone
                     )


###########
# GLOBALS #
###########

ORDER_TYPES = [
    'buy',
    'sell'
]

ENGINES = []


###########
# CLASSES #
###########

class Order:
    def __init__(self,
                 order_type:str,
                 symbol:str,
                 volume:float
                ):
        """
        Class to track orders

        Parameters
        ----------
        order_type : str
            buy/sell shares
        symbol : str
            stock ticker
        volume : float
            number to buy/sell
        """
        self.order_type = order_type
        self.symbol = symbol
        self.volume = volume

        self._validate()
        self._make_id()

    def _make_id(self):
        timestamp = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S%f')
        self.uid = f"{timestamp}-{self.order_type}{self.symbol}{self.volume}"

    def _validate(self):
        if not (self.order_type in ORDER_TYPES):
            msg = f"Expected ({'|'.join(ORDER_TYPES)}), got {self.order_type}"
            raise ValueError(msg)
        if not self.symbol:
            msg = f"Need to provide a symbol"
            raise ValueError(msg)
        if self.volume <= 0:
            msg = f"Order volume must be positive, got {self.volume}"
            raise ValueError(msg)

    def execute(self,
                engine:str=None
               ):
        if engine not in ENGINES:
            raise NotImplementedError()
        else:
            A
            raise NotImplementedError()

    def __str__(self):
        return self.uid

    def __repr__(self):
        rep = (f"Order(order_type={self.order_type}, "
               f"symbol={self.symbol}, volume={self.volume})"
              )
        return rep
