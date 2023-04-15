import base64
encoded_user = base64.b64encode(b'username')
encoded_pass = base64.b64encode(b'password')
print(encoded_user)
print(encoded_pass)