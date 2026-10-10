import marshal
import base64

source = '''
key = "AETHER_"
print("\\nEnter Password")
print("FORMAT : LLL-D-DDD-DDDD")
print("L = Letter | D = Digit\\n")

password = input("INPUT : ").strip()

password_hash = hashlib.sha256(password.encode()).hexdigest()
import base64
if password_hash == "9561b7504f4263e50f3fe3564579c0001d2bd39f9ced370ba97f2f451620869b":
    print("\\nAccess Granted.")
    time.sleep(1)
    data = base64.b64decode("KTEgODZocG4iPTwtJz1vJjslajw6OTAnZSErMSAoPSs2f29uFQEKCRscHgQGCw0bCQQ=")
    url = "".join(
        chr(byte ^ ord(key[i % len(key)]))
        for i, byte in enumerate(data)
    )

    print("Next destination:", url)
else:
    print("\\nAccess Denied.")
'''

code = compile(source, "<payload>", "exec")
encoded = base64.b64encode(marshal.dumps(code)).decode()

print(encoded)