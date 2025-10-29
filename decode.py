import base64
def decode_pass(password):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode()
    print(f"decoded password {decode_data}")
encoded_string = input("enter the base64 string: ")
decode_pass(encoded_string)