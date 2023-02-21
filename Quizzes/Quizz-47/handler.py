from passlib.context import CryptContext

pwd_config = CryptContext(schemes=["pbkdf2_sha256"])

def encrypt_password(base, inhabitant, income_tax, pension, health, total):
    string = f"base{base},inhabitant{inhabitant},income_tax{income_tax},pension{pension},health{health},total{total}"
    print(string)
    return pwd_config.hash(string)
    #return "test"

print(encrypt_password(100000, 4, 3, 2, 1, 90000))
