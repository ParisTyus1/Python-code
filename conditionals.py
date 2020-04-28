# is_hot = True
# is_cold = False
# if is_hot:
#     print("It's a hot day")
#     print("Drink Your Water")
#     print("Enjoy Your Day")
# elif is_cold:
#     print("its Cold, Dress warm")
#     print("Stay warm")
#     print("Enjoy Your Day")
# else:
#     print("Enjoy Your day")
#
# price = 1000000
# has_good_credit = True
# # has_high_income = True
# has_criminal_record = True
#
# if has_good_credit and not has_criminal_record:
#     print("eligible for loan")
#
# if has_good_credit:
#     down_payment = 0.1 * price
# elif has_bad_credit:
#     down_payment = 0.2 * price
# else:
#     down_payment = 0
# print(f"Down Payment: ${down_payment}")

# temperature = 35
# if temperature != 30:
#     print("it is a hot day")
# else:
#     print("its not hot")

# name = "john smith"
# # if  len(name) < 3:
# #     print("name must be at least 3 characters")
# # elif len(name) > 50:
# #     print("name is too big")
# # else:
# #     print("name looks good")


weight = int(input("Weight: "))
unit = input('(L)bs or (K)g:  ')
if unit.upper() == "L":
   converted =  weight * 0.45
   print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")