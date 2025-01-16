def rev_order(num):
    revno = ""
    if num <= 0:
        raise ValueError("Please enter a positive integer greater than 0.")
    
    while num > 0:
        revno += f"{num}\n"
        num -= 1

    return revno.strip()

try:
    number = int(input("Enter the number, homie..! : "))
    print(rev_order(number))
except ValueError as ve:
    print(ve)
except Exception as e:
    print("An unexpected error occurred:", e)
