val = 5

def multiplier(x):
    return x * 2

for i in range(3):
    print(val)
    val = multiplier(val)

print(val)
