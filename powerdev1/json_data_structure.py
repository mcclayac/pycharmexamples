"""
        
   created: mcclayac
   Company Name : BigMAN Software
   MyName: Tony McClay
   date: 11/21/18
   day of month: 21
   
   Project Name: pycharmexamples
   filename:  
   package name: 
   IDE: PyCharm
   
   
"""
import json

class MenuItem():
    """
    This is a menu Item for my store

    """

    def __init__(self, aMenuItem, theCost, theMarkup, theMotivation):
        self.menuItem =  aMenuItem
        self.cost = theCost
        self.markup = theMarkup
        self.motivation = theMotivation
        self.family = 0.0

    def setFamilyDiscount(self, family_discount):
        self.family = family_discount

    def price(self):
        discount = self.cost * self.family
        return (self.cost * self.markup) - discount

menu = []
menu.append( MenuItem("Big Boy", 3.45, 1.25, "Tony's Favorite"))
menu.append(  MenuItem("Cowboy", 5.45, 1.20, "Football team"))
menu.append(  MenuItem("Davita", 5.45, 1.20, "Sucks you dry"))

with open('../json_examples/menu.json', 'w') as f:
    data = json.dump(menu, f)


