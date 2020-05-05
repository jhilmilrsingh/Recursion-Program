def factorial(number):
    if number <= 1:
        return 1
    else: 
        return number*factorial(number-1)
        
def main():
    
    while True:
        number = input("Enter an integer or Q to quit: ")

        if number.upper() == "Q":
            print("Good bye.")
            break
        
        if number.lower() == "q":
            print("Good bye.")
            break
        try:
            i = int(number)
        except:
            print("You must enter a valid integer. Try again")
            continue

        answer = factorial(i)
        print("The factorial of", number, "is:", answer)
        
main()
        


