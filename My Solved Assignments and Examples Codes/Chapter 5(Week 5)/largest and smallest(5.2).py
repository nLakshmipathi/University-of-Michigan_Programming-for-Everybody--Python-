largest = None
smallest = None
while True:
    inp = raw_input("Enter a number: ")

    # Handle the edge Cases
    if inp == "done" : break
    if len(inp) < 1: break                      # (Ideom) Check for Empty Line

    # Do the work
    try:
        num = int(inp)

    except:
        print 'Invalid Input'
        continue
   # print num
    if smallest is None:
        smallest = num
    elif largest is None:
        largest = num

    elif largest < num:
        largest = num

    elif smallest > num:
        smallest = num

print "Maximum is", largest
print "Minimum is", smallest





