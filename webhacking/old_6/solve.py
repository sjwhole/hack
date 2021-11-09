import base64

id = "admin"
id_byte = id.encode("ascii")
pw = "nimda"
pw_byte = pw.encode("ascii")
for _ in range(20):
    id_byte = base64.b64encode(id_byte)
    pw_byte = base64.b64encode(pw_byte)

print("id: " + id_byte.decode("ascii"))
print("password: " + pw_byte.decode("ascii"))
