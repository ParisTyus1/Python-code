# sale exercise #

lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 
32 inches high X 40 inches wide x 30 inches deep. Red or White
"""

lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Settee. Faux leather on birch. 
29.50 inches high x 54.75 inches wide x 28 inches deep. Black
"""

stylish_settee_price = 108.50

luxurious_lamp_description = """ 
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""

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
# ---------------------------------------- #


# physics --- force & work  #
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1


def get_force(mass, acceleration):
    return mass * acceleration


train_force = (get_force(train_mass, train_acceleration))
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force")


def get_energy(mass, c=3 * 10 ** 8):
    return mass * c ** 2


bomb_energy = get_energy(bomb_mass)
print(bomb_energy)
print("The 1Kg bomb supplies " + str(bomb_energy) + " Joules")


def get_work(mass, acceleration, distance):
    get_force = mass * acceleration
    result = get_force * distance
    return result


train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)
print("The GE train does " + str(train_work) + " Joules of work over" + str(train_distance) + " meters")


# ---------------------------------------------------- #

# Temperature conversion #
def f_to_c(f_temp, c_temp):
    c_temp = (f_temp - 32 * 5 / 9)
    return c_temp


f100_in_celsius = f_to_c
f_temp = 100

print(f_to_c(100, 0))


def c_to_f(c_temp, f_temp):
    f_temp = (c_temp * (9 / 5) + 32)
    return f_temp


c0_in_fahrenhiet = c_to_f
c_temp = 0

print(c_to_f(0, 100))


# ----------------------------------#
# Write a function called greater_than that takes two integer inputs,
# x and y and returns the value that is greater.
# If x and y are equal, return the string

# Codecademy conditionals #
def greater_than(x, y):
    if x > y:
        return x
    if y > x:
        return y
    if x == y:
        return "These numbers are the same"


# The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it)
# requires students to earn 120 credits to graduate.
# Write a function called graduation_reqs
# that takes an input credits and checks if the
# student has enough credits to graduate. If they do, return the string

def graduation_reqs(credits):
    if credits >= 120:
        return "You have enough credits to graduate!"


# Call graduation_reqs with an input of 120 credits and print the result to the terminal.
# Can a student with 120 credits graduate from Calvin Coolidge’s Cool College?
print(graduation_reqs(120))
