import jwt
import time
from pathlib import Path

# Define Snowflake account details
account_identifier = "vyb82036"
user = "CORTEXSA"

# Define the full path to your private key
private_key_path = Path("C://Users//User//Documents//snowsql//rsa_key.p8").read_text()

# JWT expiration time (current time + 60 seconds)
current_time = int(time.time())
expiration_time = current_time + 60  # JWT expires after 60 seconds

# Define the token headers and payload
headers = {
    "alg": "RS256"
}

payload = {
    "iss": f"{account_identifier}.{user}",  # Issuer (account.identifier.user)
    "sub": user,  # Subject (Snowflake user)
    "iat": current_time,  # Issued At
    "exp": expiration_time  # Expiration time
}

# Generate the JWT using the private key
jwt_token = jwt.encode(payload, private_key_path, algorithm="RS256", headers=headers)

print("Generated JWT Token:")
print(jwt_token)
