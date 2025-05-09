num1 = 10
num2 = 25

if num1 > num2:
    print(str(num1) + " is greater than num2")
else: 
    print(str(num2) + " is greater than num1")


numbers = [1,2,3,4,5,6,7,8,9,10];

def evenOrNot(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(str(num) + " is even number")
        else:
            print(str(num) + " is odd number")
            
def getAverage(numbers):
    result = sum(numbers) / len(numbers)
    print(result);


getAverage();
evenOrNot(numbers);
