# Convert integer 65 to ASCII Character ('A') 
y = chr(65)
print(y)
# Convert ASCII Unicode Character 'A' to 65 
z = ord('A')
print(z)
def encode(string):
    result = ''
    bytes_string = string.encode()
    for char in bytes_string:
        result += format(char,'#02x').zfill(2)
    return result

# def decode():


print(encode("MarkIsGay"))