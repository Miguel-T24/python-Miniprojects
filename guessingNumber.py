import random as rand
number = round(rand.random() * 100)
print("""
        If you enter a wrong number, I will guide you with an arrow so you can guess
        ↟ when you should place a higher number  and
        ↡ when you should place a lower number
""")
while True:
    try:
        guess = int(input("Enter a number: "))
    except:
        print("Value is valid, try Again! ")
    else:
        while True:
            if guess == number:
                print("You Win! ")
                break
            else:
                if number < guess:
                    guess = int(input("↡  Try Again: "))
                else:
                    guess = int(input("↟  Try Again: "))
        break