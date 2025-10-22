# The function we want to test
def add(a, b):
    return a + b

# Test 1: Basic addition
assert add(2, 3) == 5
print("Test 1 passed! ✅")

# Test 2: Adding zero
assert add(5, 0) == 5
print("Test 2 passed! ✅")

# Test 3: Negative numbers
assert add(-2, 3) == 1
print("Test 3 passed! ✅")

print("All tests passed! 🎉")
