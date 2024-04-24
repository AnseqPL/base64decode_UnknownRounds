import base64

def decode_base64(data):
    try:
        return base64.b64decode(data)
    except base64.binascii.Error:
        return None

# open file
with open("base64file.txt", "rb") as file:
    encoded_data = file.read()

decoded_data = encoded_data
rounds = 0

# decoding
while True:
    result = decode_base64(decoded_data)
    if result is not None:
        decoded_data = result
        rounds += 1
    else:
        break

print(f"Decoded after: {rounds} rounds coding Base64.")

# write to file
with open("decoded_file.txt", "wb") as output_file:
    output_file.write(decoded_data)