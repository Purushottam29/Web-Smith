**Check if a Number is Even or Odd in Python**
====================================================

This code will take an integer as input and determine whether it is even or odd.

```python
def check_even_odd(num):
    """
    Check if a number is even or odd.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    str: The result of the check, e.g., 'even' or 'odd'.
    """
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# Example usage
num = int(input("Enter a number: "))
result = check_even_odd(num)
print(f"{num} is {result}.")
```

**Explanation**
---------------

1. We define a function `check_even_odd` that takes an integer `num` as input.
2. We use the modulus operator `%` to find the remainder of `num` divided by 2.
3. If the remainder is 0, the number is even, so we return the string "even".
4. Otherwise, the number is odd, so we return the string "odd".
5. In the example usage, we use `input` to get a number from the user, pass it to the `check_even_odd` function, and print the result.

**Alternative Solution**
------------------------

You can also use a conditional expression to make the code more concise:

```python
def check_even_odd(num):
    """
    Check if a number is even or odd.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    str: The result of the check, e.g., 'even' or 'odd'.
    """
    return "even" if num % 2 == 0 else "odd"

# Example usage
num = int(input("Enter a number: "))
print(f"{num} is {check_even_odd(num)}.")
```