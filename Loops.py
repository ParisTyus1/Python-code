# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess :'))
#     guess_count +=1
#     if guess == secret_number:
#         print("you won")
#         break
# else:
#     print("Sorry you failed")

# command = ""
# started = False
# stopped = False
# while True:
#     command = input(">").lower()
#     if command == "start":
#         if started:
#             print("Car Started")
#         else: started = False
#         print("Car is already started!!")
#     elif command == "stop":
#         if stopped:
#             print("Car Stopped")
#         else: stopped = True
#         print("Car is already Stopped!!")
#     elif command == "help":
#         print("""
#         start - to start the car
#         stop - to stop the car
#         quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I dont understand")

# for item in range(2,20, 2):
#     print(item)
#
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total : {total}")
#
# for x in range (4):
#     for y in range(3):
#         print(f'{x}, {y})')
#
# numbers = [5, 2, 15, 2, 2]
# total = 0
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += "x"
#     print(output)
#
names = ['john', 'bosh', 'sarah', 'kim']
names.append('paris')
print(names)

max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# two dimensional list
import row

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]

]
# loop within a loop #
for item in matrix:
    for item in row:
            print(item)


matrix[0][1] = 20
print(matrix)