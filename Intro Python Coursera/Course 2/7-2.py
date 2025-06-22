# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
linecount = 0
totalconf = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    linecount = linecount + 1
    tokens = line.split()
    for word in tokens:
        try:
            conf = float(word)
            totalconf = totalconf + conf
        except:
            continue

print("Average spam confidence:", totalconf / linecount)
