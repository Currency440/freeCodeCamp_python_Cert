def number_pattern(n):
    # 1. Check if the input is an integer (specifically excluding booleans)
    if not isinstance(n, int) or isinstance(n, bool):
        return "Argument must be an integer value."
    
    # 2. Check if the integer is at least 1
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    # 3. Generate the pattern using a list comprehension and join
    # This prevents the trailing space issue
    pattern = " ".join(str(i) for i in range(1, n + 1))
    
    return pattern
print( number_pattern(4))
print( number_pattern(12))
print( number_pattern(4.5))
print( number_pattern(-3))