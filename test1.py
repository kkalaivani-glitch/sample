def add(a, b):
    return a * b  # BUG: Should be + not *

# This will FAIL
assert add(2, 3) == 5
