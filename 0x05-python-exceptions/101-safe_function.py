#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        a = fct(*args)
        return a
    except (ValueError, TypeError, Exception) as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return None
