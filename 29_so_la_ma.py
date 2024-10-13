def from_roman_numeral(roman):
    # Cac gia tri trong so La Ma
    roman_to_decimal = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Duyệt tung ki tu cua so La Ma
    for char in reversed(roman):
        value = roman_to_decimal[char]
        
        # Theo naming rule: Neu gia tri hien tai nho hon gt truoc 
        # thi tru gia tri do di
        if value < prev_value:
            total -= value
        else:
            total += value
            
        prev_value = value
    
    return total

# Example
print(from_roman_numeral("XIV"))  
print(from_roman_numeral("MCMXCIV"))  
