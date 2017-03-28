def parent(num):
    """
    Example in nesting function
    Args:
        num: integer
    Returns:
        returns a function
    Raises:
        AssertionError: Raises an exception
    """
    value = 3
    def first_child():
        return "Printing from the first_child() function. " + str(value)

    def second_child():
        return "Printing from the second_child() function. " + str(num)

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child

foo = parent(10)
bar = parent(11)

print(foo)
print(bar)

print(foo())
print(bar())
