from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Generar una clave y un vector de inicialización (IV)
# La clave debe ser de 16, 24 o 32 bytes (128, 192 o 256 bits)
key = os.urandom(32)  # 256 bits
iv = os.urandom(16)   # 128 bits

# Función para encriptar
#Valores para generar el cifrado

key = b'\x1a\xf3\x8c\xd7\xe2\x9a\xb4\x12\x45\x67\x89\xab\xcd\xef\x01\x23\x45\x67\x89\xab\xcd\xef\x01\x23\x45\x67\x89\xab\xcd\xef\x01\x23'
iv = b'\x0f\xe2\x4a\x7b\x8c\xd9\xa1\xb2\xc3\xd4\xe5\xf6\x07\x18\x29\x3a'


def encrypt(plaintext):
	key = b'\x1a\xf3\x8c\xd7\xe2\x9a\xb4\x12\x45\x67\x89\xab\xcd\xef\x01\x23\x45\x67\x89\xab\xcd\xef\x01\x23\x45\x67\x89\xab\xcd\xef\x01\x23'
	iv = b'\x0f\xe2\x4a\x7b\x8c\xd9\xa1\xb2\xc3\xd4\xe5\xf6\x07\x18\x29\x3a'
	 # Crear un objeto Cipher con AES en modo CBC
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
	encryptor = cipher.encryptor()

	 # Aplicar padding al texto plano para que sea múltiplo del tamaño del bloque (16 bytes)
	padder = padding.PKCS7(algorithms.AES.block_size).padder()
	padded_data = padder.update(plaintext.encode()) + padder.finalize()

	# Encriptar los datos
	ciphertext = encryptor.update(padded_data) + encryptor.finalize()
	return ciphertext

# Función para desencriptar
def decrypt(ciphertext):
	key = b'\x1a\xf3\x8c\xd7\xe2\x9a\xb4\x12\x45\x67\x89\xab\xcd\xef\x01\x23\x45\x67\x89\xab\xcd\xef\x01\x23\x45\x67\x89\xab\xcd\xef\x01\x23'
	iv = b'\x0f\xe2\x4a\x7b\x8c\xd9\xa1\xb2\xc3\xd4\xe5\xf6\x07\x18\x29\x3a'
	#Crear un objeto Cipher con AES en modo CBC	
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
	decryptor = cipher.decryptor()
   	# Desencriptar los datos
	padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    	# Eliminar el padding
	unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
	plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
	return plaintext.decode()

# Ejemplo de uso
'''plaintext = input("Ingresa contaseña")
ciphertext = encrypt(plaintext)
print(f"Texto encriptado: {ciphertext}")
decrypted_text = decrypt(ciphertext)
print(f"Texto desencriptado: {decrypted_text}")

'''
