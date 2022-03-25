"""
Purpose: Analyst base 
"""

import os


class BaseAnalyst:
    def __init__(self, uid, portfolio, strategy):
        self.uid = uid
        self.portfolio = portfolio
        self.strategy = strategy
