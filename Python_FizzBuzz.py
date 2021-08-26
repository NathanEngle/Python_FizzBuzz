# Nathan Engle
# August/26/2021
# Program Description: Simple FizzBuzz application.
# For any number of an arbitrary range, print "Fizz" if it is evenly divisible by 3.
# Print "Buzz" if it is divisible by 5
# And print Fizzbuzz if it is divisible by both 5 and 3

#uses variables for determining the printing of Fizz or Buzz
#this allows easily changing the conditions of when to print
fizzNum = 3
buzzNum = 5
flag = 0 #if this is changed, don't print the number

for i in range(1, 100):
    if(i % fizzNum == 0):
        print("Fizz", end = "")
        flag = 1
    if(i % buzzNum == 0):
        print("Buzz", end = "")
        flag = 1
    if(flag == 0):
        print(i, end = "")
    print("\n")
    flag = 0