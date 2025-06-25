name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

d = {}
l = []

for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    nums = words[5].split(":")
    d[nums[0]] = d.get(nums[0], 0) + 1

'''
for k, v in d.items():
    l.append((k, v))

l = sorted(l)
for k, v in l:
    print(k, v)
    '''
# Top part simplified by bottom

for k, v in sorted([(k, v) for (k, v) in d.items()]):
    print(k, v)