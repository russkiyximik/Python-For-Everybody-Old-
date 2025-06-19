val = 5

def multiplier(x):
    return x * 2

for i in range(3):
    print(val)
    val = multiplier(val)

print(val)

# Trying a new thing

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        n = int(num)
    except:
        if num == "done":
            break
        else:
            print("Invalid input")
    if largest is None and smallest is None:
            largest = n
            smallest = n
    elif n > largest:
            largest = n
    elif n < smallest:
            smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)
