def check_prime(num):  
    if num < 2:
        print(num, "is not a prime number")
        return
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            return
    print(num, "is a prime number")
n = int(input("Enter a number: "))
check_prime(n)
