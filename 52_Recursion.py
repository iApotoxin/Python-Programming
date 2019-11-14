def exp(x, n):
    if n == 0:
        return 1
    else:
        return x * exp(x, n-1)  # Recursion call exp() in exp()

print("Exponet of 2^4 = ",exp(2, 4))
