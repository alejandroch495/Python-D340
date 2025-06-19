# Alejandro Chavez
# Final part 1 
# Order class
menu_options : list[str] = ["De Anza Hamburger","The Western Burger","Bacon Cheese Burger","Don Cali Burger","Mushroom Swiss Burger"]
menu_prices : list[float] = [5.25,5.95,5.75,5.95,5.95]
class Order:
    def __init__(self, menu_options : list[str] = []):
        """### Takes in a menu list of items
        ##### and uses it for orders"""
        self._order : list = []
        self._menu_options = menu_options
        self._options = len(menu_options)

    def get_order(self) -> list:
        return self._order
    def get_options(self) -> list[str]:
        return self._menu_options
    def add_order(self):
        buger_selection = self._get_burger_option()
        if buger_selection <= len(self._menu_options):
            self._order.append((self._menu_options[buger_selection-1],self._get_quantity()))
        
    
    def _get_burger_option(self):
        _counter = 0
        for burger in self._menu_options:
            _counter += 1
            print(f'{_counter}. {burger}')
        while True:
            try:
                user_input = int(input(f'Enter a burger option from above. Enter {len(self._menu_options)+1} to finish/exit order: ').strip())
                return user_input
            except:
                print(f"\n-------Please enter a number from 1 - {len(self._menu_options)}\nEnter {len(self._menu_options)+1} when finished ordering!")

    
    def _get_quantity(self):
        while True:
            try:
                user_input = int(input('Please enter a quantity: ').strip())
                if user_input > 0:
                    return user_input
                else:
                    print("Enter a positive number!")
            except: 
                print("Enter a positive numerical value!")


def repeat_order(customer:Order):
    counter =0
    order_list = customer.get_order()
    for order in order_list:
        counter += 1
        print(f'{counter}. {order[0]} - {order[1]}')    
    

def main():
    customer = Order(menu_options = menu_options)
    customer.add_order()
    repeat_order(customer)
    print()
if __name__ == "__main__":
    main()