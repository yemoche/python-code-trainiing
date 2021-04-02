def mathsOperation(value1, value2):
    return value1/value2

try:
    value1 = int(input("Enter first number:"))
    value2 = int(input('Enter second number:'))

    divisionOfNumbers = mathsOperation(value1, value2)
    print(divisionOfNumbers)
except ZeroDivisionError as err :
    print('Error', err)
else:
    print('code is good to go')

