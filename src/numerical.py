def add_numbers(a = 7,  b = 8):
    """
    add the numbers together

    Arguments:
        a: one number
        b: the other number

    Returns:
        float: the addition of the two numbers
    """
    if isinstance(a, str) or isinstance(b, str):
        raise NotImplementedError('This function only takes numerical values')
    def add_numbers_inner(a, b):
        sum = float(a) + float(b)
        return sum
    return add_numbers_inner(a, b)

