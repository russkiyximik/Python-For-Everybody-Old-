import re
handle = open('redata.txt')
nums = 0

for line in handle:
    stuff = re.findall("[0-9]+", line)
    for i in range(len(stuff)):
        nums = nums + int(stuff[i])

print(nums)

# Another way to do it:
# new_list = [expression for item in iterable]

print(sum( [ int(i) for i in re.findall('[0-9]+',open('redata.txt').read()) ] ) )