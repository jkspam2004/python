
# print fizzbuzz if number divisible by 15
# print fizz if number divisible by 3
# print buzz if number divisible by 5
# else print the number

for i in range(1,16) :
    if (i % 15 == 0) :
        print("FizzBuzz")
    elif (i % 3 == 0) :
        print("Fizz")
    elif (i % 5 == 0) :
        print("Buzz")
    else :
        print(i)
