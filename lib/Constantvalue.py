def solve(word):
    vowels = "aeiou"
    consonant_values = [sum(ord(char) - ord('a') + 1 for char in substring) for substring in ''.join([' ' if char in vowels else char for char in word]).split()]

    return max(consonant_values, default=0)

# Example tests
print(solve("zodiacs"))  # Output: 26
print(solve("strength"))  # Output: 57
