
num = int(input("Write a number: "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"This is the prime number")
    summation = ((num+1)*num)//2
    print(f"Sum from 0 to {num} is {summation}")

