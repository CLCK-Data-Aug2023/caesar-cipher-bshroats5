def caesar_cipher(text):
   result = ""
   for char in text:
       if char.isalpha(): # Check if the character is a letter
           ascii_offset = ord('A') if char.isupper() else ord('a') # Get ASCII offset for uppercase or lowercase
           shifted_char = chr((ord(char) - ascii_offset + 5) % 26 + ascii_offset) # Apply Caesar cipher with shift of 5
           result += shifted_char
       else:
           result += char # Keep non-alphabetic characters unchanged
   return result

# Ask user for input
plain_text = input("Please enter a sentence:")

# Encrypt the input using Caesar cipher with a right shift of 5
encrypted_text = caesar_cipher(plain_text)

# Print the encrypted text
print(f"The encrypted sentence is: {encrypted_text}") 
