class Product:
    def __init__(self, name, price):
        
              
        if type(name)==str and type(price)==float and price>=0:
            self.name = name 
            self.price = price 
        elif type(name)!=str:
            raise TypeError    
        elif type(price)!=float:
            raise TypeError 
        elif price<0:
            raise ValueError    
