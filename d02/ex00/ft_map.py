from collections.abc import Iterable


def ft_map(function_to_apply, iterable):
    if not isinstance(iterable, Iterable):
        return None
    try:
        for elt in iterable:
            yield function_to_apply(elt)
    except TypeError:
        raise TypeError('raise Type Error')
