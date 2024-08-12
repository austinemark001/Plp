price = input('Enter price:')
discount_percentage('Ented discount percentage:')

def calculate_discount(price, discount_percentage):
   if discount_percentage >= 20:
       return price - (price * discount_percentage/100)
   return price

print(calculate_discount(price, discount_percentage))
