"""
Purpose: Class to represent orders
"""

from datetime import datetime


class Order:
    def __init__(self,
                 coin: str,
                 order_type: str,
                 quantity: float,
                 value_at_order: float,
                 approver: str
                ):
        self.coin = coin

        assert order_type in ['BUY','SELL'], f"Bad order type, expect {order_type}"
        self.order_type = order_type
        self.quantity = quantity
        self.value_at_order = value_at_order
        self.approver = approver

        self.expected_delta = self.quantity * self.value_at_order

    def execute(self):
        # Something to actually execute the order
        self._set_execution_time()

    def _set_execution_time(self):
        self.execution_time = datetime.now()

    def _find_value_at_execution(self):
        """
        The value at the time the order was actually executed
        """
        self.value_at_execution = None
        self.actual_delta = self.quantity * self.value_at_execution

    def _find_total_value(self,
                          value: float
                         ) -> float:
        if self.order_type == 'BUY':
            scalar = -1
        elif self.order_type == 'SELL':
            scalar = 1
        total_value = scalar * self.quantity * value
        return round(total_value, 6)

    def __repr__(self):
        expected_change = self._find_total_value(self.value_at_order)
        actual_change = self._find_total_value(self.value_at_execution)
        rep = f"{self.order_type} {self.quantity} {self.coin} for {self.value_at_order}\n"
        rep += f"-Expected Change: {expected_change}\n"
        rep += f"-Actual Change: {actual_change}\n"
        rep += f"-Difference: {actual_change - expected_change}\n"
        rep += f"-Executed on: {self.execution_time}\n"
        rep += f"-Approved by: {self.approver}"
