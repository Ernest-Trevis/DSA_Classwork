upperbound = int(input("Enter Upperbound:"))
lowerbound = int(input("Enter Lowerbound:"))

if upperbound >=lowerbound:
    while upperbound >= lowerbound:
        print(upperbound)
        upperbound-=1

else:
    print("Upperbound cannot be less than lowerbound!")