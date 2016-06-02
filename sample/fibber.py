#Generates first 30 fibonacci
#f = f(n-1) + f(n-2)


def fibber(x):
    if x >= 2:
        return fibber(x-1) + fibber(x-2)
    return x
