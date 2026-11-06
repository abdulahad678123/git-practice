import random

arr = random.sample(range(1, 50), 10)
print(arr)

largest = 0
ndlarg = 0

for num in arr:
    if num > largest:
        ndlarg = largest
        largest = num

    elif num > ndlarg:
        ndlarg = num

print("Largest number after loop end is: ", largest)
print("Largest number after loop end is: ", ndlarg)
