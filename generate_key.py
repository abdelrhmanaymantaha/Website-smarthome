import secrets
import base64

print(base64.urlsafe_b64encode(secrets.token_bytes(32)).decode('utf-8'))