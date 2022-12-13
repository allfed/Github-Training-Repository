def bumpy_reduction(x,recursions = 5):
    """
    This function is a recursive function that does some whacky things that I can't explain
    Arguments:
        x: input number
        recursions: must be a positive int, default is 5 if noit specified, is the number of times the function will recurse
    Returns:
        recursive function: if recursions is 0, returns x, otherwise returns bumpy_reduction(x/2 + recursions**2, recursions - 1)
    """
    if type(recursions) != int or recursions < 0:
        raise NotImplementedError('fib only defined on non-negative integers.')
    elif recursions == 0:
        return x
    else:
        return bumpy_reduction(x/2 + recursions**2, recursions - 1)

