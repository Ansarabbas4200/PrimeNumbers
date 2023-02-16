num = int(input("Write a number: "))


def sum_prime(n):
    is_prime = True
    for i in range(2, n):
        if num % i == 0:
            is_prime = False
    if is_prime:
        summation = ((n + 1) * n) // 2
        return f"This is a prime number.\nSum from 0 to {n} is {summation}"
    else:
        return -1


numbers_sum = sum_prime(num)
print(numbers_sum)
