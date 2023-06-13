#!/usr/bin/python3
"""Subclass MyInt inherits parent Int"""

class MyInt(int):
    """invert int operators"""

    def __eq__(self, other):
        """replace == with !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """replace != with =="""
        return super().__eq__(other)
