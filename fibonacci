def fib_recursive(n):
    if n in [0, 1]:
        return n
    print("computing fib_recursive(%i)" % n)
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n):

    # edge case
    if n < 0:
        raise Exception("Index was negative. No such thing as a negative index in a series.")

    # base cases
    elif n in [0, 1]:
        return n

    prev = 0
    prev_prev = 1

    for _ in range(n):
        current = prev + prev_prev
        print(current)
        prev_prev = prev
        prev = current

    return current

n=input()
#print(fib_recursive(n))
print(fib_iterative(n))
