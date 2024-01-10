import hashlib

s=input()
crypto = hashlib.sha256()
crypto.update(s.encode())
hash_value = crypto.hexdigest()

print(hash_value)

