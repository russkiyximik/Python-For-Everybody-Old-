numint = []
while True:
    repeat = False
    inp = input("What are your numbers?")
    nums = inp.split()
    for num in nums:
        try:
            numint.append(int(num))
        except:
            print("Incorrect input! Try again")
            repeat = True
            break
    if repeat == False: break