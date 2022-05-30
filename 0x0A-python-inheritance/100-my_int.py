#!/usr/bin/python3
"""a class that inherits from int"""


class MyInt(int):
    """ a class int """
    def __eq__(self, init):
        return super().__ne__(init)

    def __ne__(self, init):
        return super().__eq__(init)
