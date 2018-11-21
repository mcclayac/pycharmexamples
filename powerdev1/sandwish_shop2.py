"""

This is a test module for Pycharm projects

"""
import math


class Calculator:
    """Form a Caculator.

        """
    def __init__(self, my_cost):
        """ initaion of the Cost Object

        Keyword arguments:
        my_cost -- the cost to be executed (default 0.0)
        """
        self.my_cost = my_cost

    def markup(self, rt_value):
        """ markup the item

        Keyword arguments:
        rt_value -- the cost to be executed (default 0.0)



        :returns
        int - return value
        """
        mark = math.sqrt(rt_value)
        return self.my_cost * mark

    @property
    def family(self):
        """

        family property

        :returns
        int - return value
        """
        mark = 23
        return mark


MY_COST_VALUE = sum([1.00*2, 1.50, 0.66])
MENU_INSTANCE = Calculator(MY_COST_VALUE)

CHARGE_NUMBER = MENU_INSTANCE.family
# charge = menu.markup(4)
print("PB&J costs : {}".format(str(CHARGE_NUMBER)))
