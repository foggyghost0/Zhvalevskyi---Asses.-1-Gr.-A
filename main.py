"""
PowerOfTen
"""
while True:
    input_number = int(input("Enter a max 3 digit number>> "))
    if input_number < 0:
        print(f"The number {input_number} cannot be negative.")
    elif input_number > 999:
        print(f"The number {input_number} has more than 3 digits. ")
    else:
        break

while True:
    if 0 < input_number <= 9:
        print(f"{input_number} * 1")
        continue
    elif 9 <= input_number <= 99:
        p1 = input_number // 10
        p2 = input_number % 10
        print(f"{input_number} = {p1} * 10 + {p2} * 1")
        continue
    elif 100 <= input_number <= 999:
        p1 = input_number // 100
        p2 = input_number // 10 % 10
        p3 = input_number % 10
        print(f"{input_number} = {p1} * 100 + {p2} * 10 + {p3} * 1")
    print("Program will terminate now.")
    break
"""

Cash Box
"""
while True:
    while True:
        to_pay = int(input("Amount to pay >> "))
        if to_pay <= 0:
            print("Negative payment is invalid.")
        else:
            break

    while True:
        received = int(input("Received >> "))
        if received <= 0:
            print("Negative received amount is invalid.")
        else:
            break

    change = received - to_pay

    if change <= 0:
        print("You did not pay enough.")
    else:
        print(f"Your change is: {change}")
        print("Program will terminate now.")
        break
