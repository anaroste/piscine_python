from collections.abc import Iterable


def ft_filter(function_to_apply, iterable):
    if not isinstance(iterable, Iterable):
        return None
    try:
        for elt in iterable:
            if function_to_apply(elt):
                yield elt
    except TypeError:
        raise TypeError('raise Type Error')
