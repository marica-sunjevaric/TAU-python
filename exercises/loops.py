fruits = ["apple", "orange", "pears", "cherries", "grapes"]

for i in fruits:
    print(f"Would you like {i} ?")

for number in range(1,11):
    if number ==7:
        print("We're skipping number 7.")
        continue
    print(f"Number {number}")

for number in range(1,11):
    if number == 3:
        pass
    else:
        print(f"The number is {number}")
