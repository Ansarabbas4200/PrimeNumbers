num = int(input("Write a number: "))


def sum_prime(n):
    is_prime = True
    for i in range(2, n):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"This is the prime number")
        summation = ((n + 1) * n) // 2
        print(f"Sum from 0 to {n} is {summation}")


sum_prime(n=num)
