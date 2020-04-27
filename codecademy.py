lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high X 40 inches wide x 30 inches deep. Red or White"""

lovely_loveseat_price = 254.00

stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black"""

stylish_settee_price = 108.50

luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""

luxurious_lamp_price = 52.15

sales_tax = .088
# first customer
customer_one_total = 0

customer_one_itemization = lovely_loveseat_description + luxurious_lamp_description

customer_one_total = lovely_loveseat_price + luxurious_lamp_price

customer_one_tax = customer_one_total * sales_tax

print("Customer One Items")
print(customer_one_itemization)
print("Customer One Total")
print(customer_one_tax)
# equations exercise  #

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp, c_temp):
    c_temp = (f_temp - 32 * 5/9)
    return c_temp

f100_in_celsius = f_to_c()
f_temp = 100

def c_to_f(c_temp,F_temp):
    f_temp = (c_temp *(9/5) + 32)
    return f_temp