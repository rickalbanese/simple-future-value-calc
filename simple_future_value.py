# simple_future_value.py
#   This program calculates the future value of an investment with an annually
#   compounding fixed interest rate, given a number of years based on user input.
#   By: Rick Albanese

def main():

    print(" This program will calculate the future value of your investment.")

    principal = eval(input(" Please enter how many dollars you are investing today: "))
    ip = principal # Initial principal
    time = eval(input(" Please enter how many years it will be invested: "))
    apr = eval(input(" Please enter the Annual Percentage Rate: % "))
    apr = apr * 0.01

    for j in range(time):
        principal = principal * (1 + apr)

    rp = float("{0:.2f}".format(principal)) # Rounded principal
    print(" Rounded to the nearest cent your intial investment of ${}, {} years later, will be worth ${}!".format(str(ip),str(time),str(rp)))

main()    
