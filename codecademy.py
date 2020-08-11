# # sale exercise #
#
# lovely_loveseat_description = """
# Lovely Loveseat. Tufted polyester blend on wood.
# 32 inches high X 40 inches wide x 30 inches deep. Red or White
# """
#
# lovely_loveseat_price = 254.00
#
# stylish_settee_description = """
# Stylish Settee. Faux leather on birch.
# 29.50 inches high x 54.75 inches wide x 28 inches deep. Black
# """
#
# stylish_settee_price = 108.50
#
# luxurious_lamp_description = """
# Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
# """
#
# luxurious_lamp_price = 52.15
#
# sales_tax = .088
# # first customer
# customer_one_total = 0
#
# customer_one_itemization = lovely_loveseat_description + luxurious_lamp_description
#
# customer_one_total = lovely_loveseat_price + luxurious_lamp_price
#
# customer_one_tax = customer_one_total * sales_tax
#
# print("Customer One Items")
# print(customer_one_itemization)
# print("Customer One Total")
# print(customer_one_tax)
# # ---------------------------------------- #
#
#
# # physics --- force & work  #
# train_mass = 22680
# train_acceleration = 10
# train_distance = 100
#
# bomb_mass = 1
#
#
# def get_force(mass, acceleration):
#     return mass * acceleration
#
#
# train_force = (get_force(train_mass, train_acceleration))
# print(train_force)
# print("The GE train supplies " + str(train_force) + " Newtons of force")
#
#
# def get_energy(mass, c=3 * 10 ** 8):
#     return mass * c ** 2
#
#
# bomb_energy = get_energy(bomb_mass)
# print(bomb_energy)
# print("The 1Kg bomb supplies " + str(bomb_energy) + " Joules")
#
#
# def get_work(mass, acceleration, distance):
#     get_force = mass * acceleration
#     result = get_force * distance
#     return result
#
#
# train_work = get_work(train_mass, train_acceleration, train_distance)
# print(train_work)
# print("The GE train does " + str(train_work) + " Joules of work over" + str(train_distance) + " meters")
#
#
# # ---------------------------------------------------- #
#
# # Temperature conversion #
# def f_to_c(f_temp, c_temp):
#     c_temp = (f_temp - 32 * 5 / 9)
#     return c_temp
#
#
# f100_in_celsius = f_to_c
# f_temp = 100
#
# print(f_to_c(100, 0))
#
#
# def c_to_f(c_temp, f_temp):
#     f_temp = (c_temp * (9 / 5) + 32)
#     return f_temp
#
#
# c0_in_fahrenhiet = c_to_f
# c_temp = 0
#
# print(c_to_f(0, 100))
#
#
# # ----------------------------------#
# # Write a function called greater_than that takes two integer inputs,
# # x and y and returns the value that is greater.
# # If x and y are equal, return the string
#
# # Codecademy conditionals #
# def greater_than(x, y):
#     if x > y:
#         return x
#     if y > x:
#         return y
#     if x == y:
#         return "These numbers are the same"
#
#
# # The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it)
# # requires students to earn 120 credits to graduate.
# # Write a function called graduation_reqs
# # that takes an input credits and checks if the
# # student has enough credits to graduate. If they do, return the string
#
# def graduation_reqs(credits):
#     if credits >= 120:
#         return "You have enough credits to graduate!"
#
#
# # Call graduation_reqs with an input of 120 credits and print the result to the terminal.
# # Can a student with 120 credits graduate from Calvin Coolidge’s Cool College?
# print(graduation_reqs(120))
#
# # boolean expressions #
# statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
#
# statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
#
#
# # Let’s return to Calvin Coolidge’s Cool College.
# # 120 credits aren’t the only graduation requirement,
# # you also need to have a GPA of 2.0 or higher.
# # Rewrite the graduation_reqs function so it takes two inputs,
# # gpa and credits, and checks to see if a student meets both requirements using an and statement.
# def graduation_reqs(gpa, credits):
#     if credits >= 120 and gpa >= 2.0:
#         return "You meet the requirements to graduate!"
#
#
# # The registrars office at Calvin Coolidge’s Cool College has another request.
# # They want to send out a mailer with information on the commencement
# # ceremonies to students who have met at least one requirement for
# # graduation (120 credits and 2.0 GPA).
# # Write a function called graduation_mailer that takes two inputs,
# # gpa and credits and checks if a student either has
# # 120 or more credits or a GPA 2.0 or higher and if so returns True.
#
# statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
#
# statement_two = (9 + 5 <= 15) or (7 != 4 + 3)
#
#
# def graduation_mailer(gpa, credits):
#     if credits >= 120 or gpa >= 2.0:
#         return True
#
#
# # The registrar’s office at Calvin Coolidge’s Cool College has been so
# # impressed with your work so far that they have another task for you.
# # They want you to return to the first function you wrote,
# # graduation_reqs, and add in several checks using and and not statements.
#
# # If a student meets both requirements the function should return
# # "You meet the requirements to graduate!"
# # If a student’s GPA is greater or equal to 2.0 but they don’t have enough credits the function should return
# # "You do not have enough credits to graduate."
# # If they have enough credits but their GPA is less than 2.0 the function should return
# # "Your GPA is not high enough to graduate."
# # If they do not have enough credits and their GPA is less than 2.0, the function should return
# # "You do not meet either requirement to graduate!"
# # Make sure your return value matches those strings exactly.
# # Capitalization, punctuation, and spaces matter!
#
# statement_one = False
#
# statement_two = True
#
#
# def graduation_reqs(gpa, credits):
#     if (gpa >= 2.0) and (credits >= 120):
#         return "You meet the requirements to graduate!"
#     if (gpa >= 2.0) and not (credits >= 120):
#         return "You do not have enough credits to graduate."
#     if not (gpa >= 2.0) and (credits >= 120):
#         return "Your GPA is not high enough to graduate."
#     if not (gpa >= 2.0) and not (credits >= 120):
#         return "You do not meet either requirement to graduate!"
#
#
# # if else statments #
# # Calvin Coolidge’s Cool College has another request for you.
# # They want you to add an additional check to the graduation_reqs function.
# # If a student is failing to meet both graduation requirements,
# # they want the function to return:
# # Use an else statement to add this to your function.
#
#
# def graduation_reqs(gpa, credits):
#     if (gpa >= 2.0) and (credits >= 120):
#         return "You meet the requirements to graduate!"
#     if (gpa >= 2.0) and not (credits >= 120):
#         return "You do not have enough credits to graduate."
#     if not (gpa >= 2.0) and (credits >= 120):
#         return "Your GPA is not high enough to graduate."
#     else:
#         return "You do not meet the GPA or the credit requirement for graduation."
#
#
# # Calvin Coolidge’s Cool College has noticed that students prefer
# # to get letter grades over GPA numbers.
# # They want you to write a function called grade_converter that
# # converts an inputted GPA into the appropriate letter grade.
# # Your function should be named grade_converter, take the input gpa, and convert the following GPAs:
#
# # 4.0 or higher should return "A"
# # 3.0 or higher should return "B"
# # 2.0 or higher should return "C"
# # 1.0 or higher should return "D"
# # 0.0 or higher should return "F"
# # You can do this by creating a variable called grade.
# #
# # Then, you should use elif statements to set grade to the appropriate
# # letter grade for the gpa entered.
# #
# # At the end of the function, return grade.
#
# def grade_converter(gpa):
#     if gpa >= 4.0:
#         return "A"
#     elif gpa >= 3.0:
#         return "B"
#     elif gpa >= 2.0:
#         return "C"
#     elif gpa >= 1.0:
#         return "D"
#     else:
#         return "F"
#
#
# # Great! Nice error raising!
# # Now let’s make that error message a little more palatable.
#
# # Write a try statement and an except statement around the line of code
# # that executes the function to catch a ValueError and make the error
# # message print You raised a ValueError!
#
# def raises_value_error():
#     raise ValueError
#
#
# try:
#     raises_value_error()
# except ValueError:
#     print("You raised a ValueError!")
#
# #1. The admissions office at Calvin Coolidge’s Cool College has heard
# # about your programming prowess and wants to get a piece of it for themselves.
# # They’ve been inundated with applications and need a way to automate the filtering process.
# # They collect three pieces of information for each applicant:
#
# # Their high school GPA, on a 0.0 - 4.0 scale.
# # Their personal statement, which is given a score on a 1 - 100 scale.
# # The number of extracurricular activities they participate in.
# # The admissions office has a cutoff point for each category.
# # They want students that have a GPA of 3.0 or higher,
# # a personal statement with a score of 90 or higher,
# # and who participated in 3 or more extracurricular activities.
#
# # Write a function called applicant_selector which takes three inputs,
# # gpa, ps_score, and ec_count. If the applicant meets the cutoff
# # point for all three categories, have the function return the string:
#
# #2. Great! The admissions office also wants to give students who have
# # a high GPA and a strong personal statement a chance even if they don’t
# # participate in enough extracurricular activities.
# #
# # If an applicant meets the cutoff point for GPA and
# # personal statement score, but not the extracurricular activity count,
# # the function should return the string:
#
# #3.  Finally, for all other cases, the function should return the string:
#
# def applicant_selector(gpa, ps_score, ec_count):
#     if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
#         return "This applicant should be accepted."
#     elif gpa >= 3.0 and ps_score >= 90 and ec_count < 3:
#         return "This applicant should be given an in-person interview."
#     else:
#         return "This applicant should be rejected."
#
# # Sal's shipping program
# # First off, we need to know how much it costs to ship a
# # package of given weight by normal ground shipping.
#
# # Write a function for the cost of ground shipping.
# # This function should take one parameter, weight,
# # and return the cost of shipping a package of that weight.
#
# def ground_shipping_cost(weight):
#     flat_rate = 20.00
#     cost = weight
#     if weight <= 2.00:
#         return cost * 1.5 + flat_rate
#     elif weight >= 2.00 and weight <= 6.00:
#         return cost * 3.00 + flat_rate
#     elif weight >= 6.00 and weight <= 10.00:
#         return cost * 4.00 + flat_rate
#     else:
#         return cost + 4.75 + flat_rate
#
# print(ground_shipping_cost(8.4))
#
# # We’ll also need to make sure we include the price of premium ground shipping in our code.
# # Create a variable for the cost of premium ground shipping.
# # Note: this does not need to be a function because
# # the price of premium ground shipping does not change with the weight of the package.
#
# premium_ground_shipping = 125.00
#
#
# # Write a function for the cost of drone shipping.
# # This function should take one parameter, weight,
# # and return the cost of shipping a package of that weight.
# def drone_shipping(weight):
#     flat_rate = 0.00
#     cost = weight
#     if weight <= 2.00:
#         return cost * 4.5 + flat_rate
#     elif weight >= 2.00 and weight <= 6.00:
#         return cost * 9.00 + flat_rate
#     elif weight >= 6.00 and weight <= 10.00:
#         return cost * 12.00 + flat_rate
#     else:
#         return cost + 14.25 + flat_rate
#
# print(drone_shipping(1.5))
#
# # Using those two functions for ground shipping
# # cost and drone shipping cost, as well as the cost
# # of premium ground shipping, write a function that
# # takes one parameter, weight and prints a statement that tells the user
#
# # The shipping method that is cheapest.
# # How much it would cost to ship a package of said weight using this method.
#
# # Great job! Now, test your function!
#
# # What is the cheapest method of shipping a 4.8 pound package and how much would it cost?
#
# # What is the cheapest method of shipping a 41.5 pound package and how much would it cost?
#
# def best_price(weight):
#     return weight
#
# print(""" The cheapest shipping method for a 4.8 pound package
# is using ground shipping and it will cost """ )
#
# print(ground_shipping_cost(4.8))
#
# print("""The cheapest shipping method for a 4.8 pound package
# is using premium ground shipping and it will cost """ )
#
# print(premium_ground_shipping)
#
# # //////////////////manipulating list //////////////////////
# names = ['Jenny', 'Alexus', 'Sam', 'Grace']
# dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
#
# names_and_dogs_names = zip(names, dogs_names)
#
# list_of_names_and_dogs_names = list(names_and_dogs_names)
#
# print(list(list_of_names_and_dogs_names))
#
# orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']
#
# # Create new orders here:
# # //concatenating lists//
# new_orders = orders + ['lilac', 'iris']
#
# broken_prices = [5, 3, 4, 5, 4] + [4]
#
# # 1. Modify list1 so that it is a range containing
# # numbers starting at 0 and up to, but not including, 9.
#
# # 2.Create a range called list2 with the numbers 0 through 7.
#
# list1 = range(9)
# list2 = range(8)
#
# # Modify the range function that created list1 such that it:
#
# # Starts at 5
# # Has a difference of 3 between each item
# # Ends before 15
#
# list3 = range(5, 15, 3)
#
# # Create a range object called list2 that:
#
# # Starts at 0
# # Has a difference of 5 between each item
# # Ends before 40
#
# list5 = range(0,40,5)
#
# # Maria's web design
# # Maria is entering customer data for her web design business. You’re going to help her organize her data.
#
# # Start by turning this list of customer first names into a list called first_names. Make sure to enter the names in this order:
#
# # Ainsley
# # Ben
# # Chani
# # Depak
#
# first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
#
# # Create an empty list called age.
# age = []
#
# # Depak’s age is 42. Use .append() to add 42 to age.
# age.append(42)
#
#
# # Maria needs a list of the ages for all customers. Create a new list called all_ages that adds age with the following list, containing the ages for Ainsley, Ben, and Chani:
#
# # [32, 41, 29]
# # Make sure all_ages begins with the ages for Ainsley, Ben, and Chani and ends with Depak’s age (stored in age)!
# all_ages = [32, 41, 29] + age
#
# # Create a new variable called name_and_age that combines first_names and all_ages using zip.
#
# name_and_age= zip(first_names, all_ages)
#
# # Create a range object called ids with an id number for each customer. Since there are 4 customers, so id values should go from 0 to 3.
# ids = range(0,4,3)
#
# # ///////////////////python gradebook//////////////////////
#
# last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
# # Create a list called subjects and fill it with the classes you are taking:
#
# # "physics"
# # "calculus"
# # "poetry"
# # "history"
# subjects = ['physics', 'calculus', 'poetry', 'history']
# subjects.append('computer science')
# # Create a list called grades and fill it with your scores:
#
# # 98
# # 97
# # 85
# # 88
# grades = [98, 97, 85, 88, 100]
#
# # Use the zip() function to combine subjects and grades.
#
# # Save this zip object as a list into a variable called gradebook.
# gradebook= list(zip(subjects, grades))
#
# # Your grade for visual arts just came in! You got a 93!
# # After the creation of gradebook (but before you print it out),
# # use append to add ("visual arts", 93) to gradebook.
# gradebook.append(('visual arts', 93))
# print(gradebook)
#
# # You also have your grades from last semester, stored in last_semester_gradebook.
# # Create a new variable full_gradebook with the items from
# # both gradebook and last_semester_gradebook.
# full_gradebook = gradebook + last_semester_gradebook
# print(full_gradebook)
#
#
# # ////////////////////////more list stuff////////////////
# list1 = range(2, 20, 3)
#
# # Calculate the length of list1 and save it to the variable list1_len.
# list1_len = len(list1)
# print(list1_len)
#
# # Change the range command that generates list1 so that it skips 3 instead of 2 between items.
# # How does this change list1_len? changes to 6
#
# employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
#
#
# # Use square brackets ([ and ]) to select the element
# # with index 4 from the list employees. Save it to the variable index4.
# # Use print and len to display how many items are in employees.
# index4 = employees[4]
# print(len(employees))
#
# employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
#
#
# # Use square brackets ([ and ]) to select the element with index 4 from the list employees. Save it to the variable index4.
# # Use print and len to display how many items are in employees.
#
# # Paste the following code into script.py:
# # print(employees[8])
# # What happens? Why?
# # Selecting an element that does not exist produces an IndexError.
# # In the line of code that you pasted, change 8 to a different number so that you don’t get an IndexError.
#
# index4 = employees[4]
# print(len(employees))
#
# print(employees[6])
#
# shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
# # Use print and len to display the length of shopping_list.
# # 2. Get the last element of shopping_list using the -1 index. Save this element to the variable last_element.
#
# # 3. Now select the element with index 5 and save it to the variable element5.
# # 4. Use print to display both element5 and last_element.
# print(len(shopping_list))
# last_element = shopping_list[-1]
# element5 = shopping_list[5]
# print(element5)
#
# suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
#
# beginning = suitcase[0:4]
# print(beginning)
# # 1.
# # Use print to examine the variable beginning.
#
# # How many elements does it contain?
#
# # 2.
# # Modify beginning, so that it selects the first 4 elements of suitcase.
#
# # 3.
# # Create a new list called middle that contains the middle two items from suitcase.
# # middle = suitcase[2:4]
#
# # Create a new list called start containing the first 3 elements of suitcase.
# # 2. Create a new list called end containing the final two elements of suitcase.
# suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
# start = suitcase[0:3]
# end = suitcase[4:]
# print(start, end)
#
# # Mrs. WIlson’s class is voting for class president. She has saved each student’s vote into the list votes.
# # Use count to determine how many students voted for 'Jake'. Save your answer as jake_votes.
# # Stuck? Get a hint
# # 2. Use print to examine jake_votes.
#
# votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake',
#          'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie',
#          'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
#
# jake_votes = votes.count('Jake')
#
# print(jake_votes)
#
# ### Exercise 1 & 2 ###
# addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
#
# # Sort addresses here:
# addresses.sort()
# print(addresses)
#
# ### Exercise 3 ###
# names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
# names.sort()
#
# ### Exercise 4 ###
# cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']
#
# sorted_cities = cities.sort()
# print(sorted_cities)
#
# games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
#
# #1. Use sorted to order games and create a new list called games_sorted.
#
# #2. Use print to inspect games and games_sorted. How are they different?
#
# games_sorted = sorted(games)
# print(games_sorted)
#
# inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
#
# inventory_len = len(inventory)
# first = inventory[0]
# last = inventory[-1]
# inventory_2_6 = inventory[2:6]
# first_3 = inventory[0:3]
# twin_beds = inventory.count('twin bed')
# inventory.sort()
#
#
#
#
# # ///////////////////////// Lenny's Pizza //////////////////////////
# # You work at Len’s Slice, a new pizza joint in the neighborhood.
# # You are going to use your knowledge of Python lists to organize some of your sales data.
#
# # If you get stuck during this project or would like to see an experienced developer work through it,
# # click “Get Help“ to see a project walkthrough video.
#
# # To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:
#
# # pepperoni
# # pineapple
# # cheese
# # sausage
# # olives
# # anchovies
# # mushrooms
#
# toppings = ['pepperoni', 'pineapple','cheese','sausage','olives','anchovies','mushroom']
# # To keep track of how much each kind of pizza slice costs, create a list called prices that holds:
# #
# # 2
# # 6
# # 1
# # 3
# # 2
# # 7
# # 2
# prices = [2,6,1,3,2,7,2]
#
# # Find the length of the toppings list and store it in a variable called num_pizzas.
# num_pizzas = len(toppings)
#
# # Print the string "We sell X different kinds of pizza!", with num_pizzas where the X is.
# print("We sell " + str(num_pizzas) + " kinds of pizza!")
#
# pizzas = list(zip(prices, toppings))
# print(pizzas)
#
# # Use zip to combine the two lists into a list called pizzas that has the structure:
# #
# # [(price_0, topping_0), (price_1, topping_1), (price_2, topping_2), ...]
# # In order to make the result of zip a list, do the following:
#
# # list(zip(____, ____))
# pizzas.sort()
#
# cheapest_pizza = pizzas[0]
# priciest_pizza = pizzas[-1]
# three_cheapest = pizzas[:3]
# print(three_cheapest)
# num_two_dollar_slices = prices.count(2)
# print(num_two_dollar_slices)
# print(cheapest_pizza)
# # ////////////////////////tuples//////////////////////
# students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
# students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
#
# for student in students_period_A:
#     #students_period_A.append(student)
#     students_period_B.append(student)
#     print(student)
#
# dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
# dog_breed_I_want = 'dalmatian'
#
# for breed in dog_breeds_available_for_adoption:
#     print(breed)
#     if breed == dog_breed_I_want:
#         print("They have the dog I want!")
#         break
# # ///////////// Loops in python////////////
# ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
#
# for i in ages:
#     if i < 21:
#         continue
#     print(i)
#
# # /////////////////While loops////////////
# all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
# students_in_poetry = []
#
# while len(students_in_poetry) < 6:
#     student = all_students.pop()
#     students_in_poetry.append(student)
#
# print(students_in_poetry)
#
# # //////////////////nested loops/////////////
# sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
#
# scoops_sold = 0
#
# for location in sales_data:
#     print(location)
#     for element in location:
#         scoops_sold += element
#
# print(scoops_sold)
#
# # ///////// list comprehensions///////
#
# heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
# can_ride_coaster = [height for height in heights if height > 161]
# # //////////convert temps using list comparisons/////////////
# celsius = [0, 10, 15, 32, -5, 27, 3]
#
# fahrenheit = [temp*(9/5) + 32 for temp in celsius]
#
# print(fahrenheit)
#
# # ////Loops review//////
# single_digits = range(10)
# squares = []
#
# for item in single_digits:
#     print(item)
#     squares.append(item**2)
#
# cubes = [item**3 for item in single_digits]
# print(cubes)
#
# print(can_ride_coaster)

# //////////Loops exercise/////////////
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
    total_price += price

average_price = total_price / len(prices)

print("Average Haircut Price: " + str(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue: " + str(total_revenue))
average_daily_revenue =  total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)

# Reviewing python fundamentals
#Write your function here
def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# line 3 uses while loop to determine first is an element and then if the element are odd, slice the first element off.

# Return all odds is the task
# 1. define the function with (lst) as the parameter
# 2. create a new empty list
# 3. create a for loop that finds all odd indices
# 4.append indices to new list

#Write your function here
def odd_indices(lst):
    new_list = []
    for index in range(1, len(lst), 2):
        new_list.append(lst[index])
    return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))


# bases and powers -------  exponents in loops
#Write your function here
def exponents(bases, powers):
    new_lst = []
    for base in bases:
        for power in powers:
            new_lst.append(base ** power)
    return new_lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))


# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number.
# If the sum of the elements of each list are equal, return lst1.

#Write your function here
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for number in lst1:
        sum1 += number
    for number in lst2:
        sum2 += number
    if sum1 >= sum2:
        return lst1
    else:
        return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
