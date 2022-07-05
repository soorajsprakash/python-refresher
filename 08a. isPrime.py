# --------------------------------------------------------------
# ------------------- PRIME NUMBER CHECKER ---------------------
# ------------------ (FUNCTION PARAMETERS) ---------------------
# --------------------------------------------------------------

def prime_checker(number):
    isPrime = True
    for i in range(2,number):
        if number%i == 0:
            isPrime = False
            # print("It's not a prime number.")
    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
        
n = int(input("Check this number: "))
prime_checker(n)
