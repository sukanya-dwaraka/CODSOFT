import secrets   # Provides cryptographically secure random numbers
import string    # Contains predefined character sets (letters, digits, etc.)

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """
    Generate a secure random password.
    
    Parameters:
        length (int): Length of the password (must be positive).
        use_upper (bool): Include uppercase letters (A–Z).
        use_lower (bool): Include lowercase letters (a–z).
        use_digits (bool): Include numbers (0–9).
        use_symbols (bool): Include special characters (!@#$ etc.).
    
    Returns:
        str: The generated password as a string.
    """

    # Validate length
    if length <= 0:
        raise ValueError("Password length must be a positive integer.")
    
    # Build a list of character pools based on user preferences
    pools = []
    if use_upper:
        pools.append(string.ascii_uppercase)   # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_lower:
        pools.append(string.ascii_lowercase)   # 'abcdefghijklmnopqrstuvwxyz'
    if use_digits:
        pools.append(string.digits)            # '0123456789'
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.<>?/")  # Common safe symbols

    # If no pools are enabled, we cannot generate a password
    if not pools:
        raise ValueError("At least one character category must be enabled.")
    
    # Start building the password
    password_chars = []

    # Ensure at least one character from each enabled category
    for pool in pools:
        if len(password_chars) < length:
            password_chars.append(secrets.choice(pool))
    
    # Fill the rest of the password with random characters from all enabled pools combined
    combined_pool = "".join(pools)
    while len(password_chars) < length:
        password_chars.append(secrets.choice(combined_pool))
    
    # Shuffle the characters to remove any predictable pattern
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)  # Pick a random index to swap with
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]
    
    # Join the list into a final string
    return "".join(password_chars)


# --- Example usage ---
if __name__ == "__main__":
    print("Example passwords generated with different options:\n")
    
    # Default: 12 characters, all categories enabled
    print("Default (12 chars, all categories):", generate_password())
    
    # 16 characters, no symbols
    print("16 chars, no symbols:", generate_password(length=16, use_symbols=False))
    
    # 6-digit PIN style password
    print("6 digits only:", generate_password(length=6, use_upper=False, use_lower=False, use_digits=True, use_symbols=False))
    
    # 24 characters, all categories
    print("24 chars, all categories:", generate_password(length=24))
    
    # Letters only (no numbers or symbols)
    print("12 letters only:", generate_password(length=12, use_digits=False, use_symbols=False))
