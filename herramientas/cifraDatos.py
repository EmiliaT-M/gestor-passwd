from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Generar una clave y un vector de inicialización (IV) únicos
# La clave debe ser de 16, 24 o 32 bytes (128, 192 o 256 bits)
KEY = os.urandom(32)  # 256 bits
IV = os.urandom(16)   # 128 bits

#Metodo que cifra las contrasenas
def encrypt(plaintext):
    """Encripta el texto plano."""
    try:
        # Validar que plaintext sea una cadena (str)
        if not isinstance(plaintext, str):
            raise ValueError("El texto plano debe ser una cadena (str).")

        # Crear un objeto Cipher con AES en modo CBC
        cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend())
        encryptor = cipher.encryptor()

        # Aplicar padding al texto plano (codificar a bytes primero)
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()

        # Encriptar los datos
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return ciphertext
    except Exception as e:
        print(f"Error al encriptar: {e}")
        return None
#Metodo que descifra las contrasenas
def decrypt(ciphertext):
    """Desencripta el texto cifrado."""
    try:
        # Crear un objeto Cipher con AES en modo CBC
        cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend())
        decryptor = cipher.decryptor()

        # Desencriptar los datos
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        # Eliminar el padding
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
        return plaintext.decode()  # Decodificar bytes a str
    except Exception as e:
        print(f"Error al desencriptar: {e}")
        return None

#