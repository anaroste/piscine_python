from collections.abc import Iterable


def ft_reduce(function_to_apply, iterable):
    if not isinstance(iterable, Iterable):
        return None
    try:
        for i in range(len(iterable) - 1):
            iterable[0] = function_to_apply(iterable[0], iterable[i + 1])
        return iterable[0]
    except TypeError:
        raise TypeError('raise Type Error')
