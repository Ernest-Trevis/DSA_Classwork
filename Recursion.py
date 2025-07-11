def countdown(n):
    print(n)
    if n == 1:
        return
    else:
        countdown(n - 1)

# Call the function
countdown(10)