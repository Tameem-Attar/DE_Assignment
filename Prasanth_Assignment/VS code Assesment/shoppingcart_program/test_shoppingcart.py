from product import Product
from shoppingcart import ShoppingCart
import unittest
def main():
    cart = ShoppingCart()
    apple = Product("apple", 0.5)
    banana = Product("banana", 0.3)
    cart.add_item(apple)
    cart.add_item(banana)
    print(f"Total price: ${cart.get_total_price():.2f}")
    cart.remove_item(apple)
    print(f"Total price: ${cart.get_total_price():.2f}")

class Test_shopping_cart(unittest.TestCase):
    def test_item_removing_or_not(self):
        apple=Product("apple",50.0) 
        banana=Product("banana",40.0)
        cart=ShoppingCart()
        cart.add_item(apple)
        self.assertEqual(cart.remove_item(apple),"Item succesfully removed from the cart") 
        self.assertEqual(cart.remove_item(banana),"Item is not in the cart")
    def test_item_is_adding_to_the_cart(self):
        apple=Product("apple",20.0) 
        banana=Product('banana',30.0) 
        cart=ShoppingCart() 

        self.assertEqual(cart.add_item(apple),"Item succesfully added to your cart") 
    def test_item_creating_or_not(self):
        # self.assertEqual(Product("apple",20.0),None)       
        with self.assertRaises(TypeError):
            apple=Product(True,30.0)
        with self.assertRaises(TypeError):
            apple=Product("apple","40.0")
        with self.assertRaises(ValueError):
            apple=Product("apple",-12.0)    
if __name__ == "__main__":
    main()
    unittest.main()
