def countdown(upperbound , lowerbound):
    print(upperbound)
    if upperbound == lowerbound:
        return upperbound
    else:
        countdown(upperbound-1 ,lowerbound)

countdown(5 , 1)