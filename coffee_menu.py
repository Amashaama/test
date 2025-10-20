class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }
  
  def get_price(self,item_name):
    return self.menu.get(item_name)
  
  def add_item(self,item_name,item_price):
    self.menu[item_name.lower()]=item_price