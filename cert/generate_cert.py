from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta
import os
from pathlib import Path

# Ensure cert directory exists
#path_folder = Path("cert")
path_folder = Path(__file__).resolve().parent  # Get the directory of this script
path_folder.mkdir(parents=True, exist_ok=True)
 
key_folder = path_folder / "key.pem"
cert_folder = path_folder / "server.pem"
# Check if the key and cert files already exist
if key_folder.exists() and cert_folder.exists():
    print("SSL Certificate and key already exist. No need to generate again.")
    exit(0)

# Generate private key
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Build certificate
subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "NA"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Localhost"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "MyOrg"),
    x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
])
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(subject)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Save the private key
with open(key_folder , "wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

# Save the certificate
with open(cert_folder, "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("✅ SSL Certificate and key have been successfully generated in the 'cert/' folder.")
