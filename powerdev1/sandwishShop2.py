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

    def markup(self, rt):
        """ markup the item

        Keyword arguments:
        rt -- the cost to be executed (default 0.0)



        :returns
        int - return value
        """
        mark = math.sqrt(rt)
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


my_cost2 = sum([1.00*2, 1.50, 0.66])
menu = Calculator(my_cost2)

charge = menu.family
# charge = menu.markup(4)
print("PB&J costs : {}".format(str(charge)))
