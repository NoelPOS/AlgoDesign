def egyptian_fraction(numerator, denominator):
    result = []
    while numerator != 0:
        x = (denominator // numerator) + 1
        result.append(x)
        numerator = numerator * x - denominator
        denominator *= x
    return result

numerator = 6
denominator = 14
fractions = egyptian_fraction(numerator, denominator)
print(f"Egyptian fractions: {fractions}")
