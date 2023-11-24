def solve(word):
    vowels = "aeiou"
    consonant_values = [ord(char) - ord('a') + 1 for char in word if char not in vowels]
    
    max_consonant_value = 0
    current_consonant_value = 0
    
    for value in consonant_values:
        current_consonant_value = max(0, current_consonant_value + value)
        max_consonant_value = max(max_consonant_value, current_consonant_value)

    return max_consonant_value

# Test cases
print(solve("zodiacs"))  
print(solve("strength"))  
