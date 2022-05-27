# 6 = 1+2+3 = 6 this a perfect number

Number = int(input('Enter the number'))
sum = 0
for i in range(1,Number):
    if Number%i==0:
        sum+=i
if Number == sum:
    print('given number is a Perfect Number') 
else:
    print('given number is not a Perfect Number')           