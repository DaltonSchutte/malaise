"""
Purpose: Data classes necessary to describe the positions of the portfolios
"""

import os
from datetime import datetime

class Position:
    def __init__(self,
                 coin: str,
                 quantity: float,
                 open_value: float,
                 open_date: datetime,
                 history: list=[]
                ):
        self.coin = coin
        self.quantity = quantity
        self.open_value = open_value
        self.open_date = open_date
        self.history = history

    def update_current_value(self):
        pass

    def _calculate_position_age(self):
        """
        Determines the age of the position
        """
        self.position_age = datetime.now() - self.open_date()

    def _calculate_last_change(self):
        """
        Displays the most recent change made to the position
        """
        pass

    @classmethod
    def open(cls, coin, quantity):
        """
        Opens a position
        """
