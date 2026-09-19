"""Exercise 3: Enforce a business rule.

Extend your Cart so invalid operations are rejected by the CART.

  ValueError        when qty < 1
  OutOfStockError   when the item's "available" field is False
  KeyError          when removing an item that is not in the cart

Then demonstrate each one with try/except.
"""

from exercise1 import load_menu
 

class OutOfStockError(Exception):
    """Raised when a customer tries to order an item that is unavailable."""
    pass


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        if qty < 1:
            raise ValueError("user input zero, anything that user inputed should greater than zero")

        if not item["available"]:
            raise OutOfStockError(f"{item['name']} is out of stock")
        for i in self.lines:
            if item["id"] == i["item_id"]:
                i["qty"] =  int(i["qty"] + qty)
                return

        self.lines.append({"item_id":item["id"],"name":item["name"],"price":item["price"], "qty":qty})
        # TODO: validate FIRST, then mutate.
        #   if qty < 1:                 raise ValueError(...)
        #   if not item["available"]:   raise OutOfStockError(...)
        # raise NotImplementedError

    def remove_item(self, item_id: int) -> None:
        # TODO: raise KeyError if the item is not in the cart
        for i in self.lines:
            if item_id == i["item_id"]:
                self.lines.remove(i)
                return
        raise KeyError("The user selected item is not in the cart")
        # raise NotImplementedError

    def total(self) -> float:
        return round(sum(line["price"] * line["qty"] for line in self.lines), 2)

    def __repr__(self) -> str:
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]           # available
    miso = menu[3]            # NOT available

    cart = Cart()

    try:
        print("Testing ValueError")
        cart.add_item(gyoza, 0)
    except ValueError as e:
        print(f"Rejected: {e}")
    
    try:
        cart.add_item(gyoza, 1)
        
    except ValueError as e:
        print(f"Rejected: {e}")
    # TODO: demonstrate each rejection with try/except and a readable message.
    # Example:
    # try:
    #     cart.add_item(gyoza, 0)
    # except ValueError as e:
    #     print(f"Rejected: {e}")


    try:
        print("Test OutOfStockError")
        cart.add_item(miso)
    except OutOfStockError as e:
        print(f"Rejected: {OutOfStockError(e)}")


    try:
        print("This is testing KeyError")
        cart.remove_item(miso)
    except KeyError as e:
        print(f"Rejected: {e}")