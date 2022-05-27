# 19,13,17,5,29 these are prime numbers

number = int(input('Enter the number'))
for i in range(2,number):
    if number%i==0:
        print('given number is not a prime number')
        break
else:
    print('given number is a prime number')