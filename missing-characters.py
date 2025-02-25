import string

def missingCharacters(s):
    all_digits = set("0123456789")
    all_letters = set(string.ascii_lowercase)
    
    present_chars = set(s)
    
    missing_digits = sorted(all_digits - present_chars)
    missing_letters = sorted(all_letters - present_chars)
    
    return "".join(missing_digits) + "".join(missing_letters)

if __name__ == '__main__':
    s = input().strip()  # Ensure input is properly stripped of whitespace
    result = missingCharacters(s)
    print(result)  # Directly print the output
