# encriptador.py
# BCY0010 - Act 1.1: Encriptador simple con PyCryptodome
# Alumno/a: [Tu nombre]

import os
import sys
import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def generar_llave(ruta_llave="llave.key"):
    """
    Genera una llave AES-256 (32 bytes) aleatoria
    y la guarda en un archivo.
    """
    llave = get_random_bytes(32)  # 256 bits
    with open(ruta_llave, "wb") as f:
        f.write(llave)
    print(f"Llave generada: {llave.hex()}")
    print(f"Tamaño: {len(llave) * 8} bits")
    print(f"Guardada en: {ruta_llave}")
    return llave


def cifrar(texto_plano, llave):
    """
    Cifra un texto plano usando AES-256 en modo CBC.
    Retorna el IV + texto cifrado en base64.
    """
    if isinstance(texto_plano, str):
        texto_plano = texto_plano.encode("utf-8")

    iv = get_random_bytes(AES.block_size)  # 16 bytes
    cifrador = AES.new(llave, AES.MODE_CBC, iv)

    texto_padded = pad(texto_plano, AES.block_size)
    cyphertext = cifrador.encrypt(texto_padded)

    resultado = base64.b64encode(iv + cyphertext)

    print(f"IV: {iv.hex()}")
    print(f"Cyphertext ({len(cyphertext)} bytes): {cyphertext.hex()[:64]}...")

    return resultado


def descifrar(datos_cifrados, llave):
    """
    Descifra datos cifrados con AES-256 CBC.
    Espera IV + cyphertext codificados en base64.
    """
    datos_raw = base64.b64decode(datos_cifrados)

    iv = datos_raw[:AES.block_size]
    cyphertext = datos_raw[AES.block_size:]

    descifrador = AES.new(llave, AES.MODE_CBC, iv)

    texto_padded = descifrador.decrypt(cyphertext)
    texto_plano = unpad(texto_padded, AES.block_size)

    return texto_plano.decode("utf-8")


def cifrar_archivo(ruta_entrada, ruta_salida, llave):
    """Cifra un archivo de texto plano (máx 1 KB)."""
    with open(ruta_entrada, "r", encoding="utf-8") as f:
        contenido = f.read()

    if len(contenido.encode("utf-8")) > 1024:
        print("Error: El archivo excede 1 KB.")
        return None

    resultado = cifrar(contenido, llave)
    with open(ruta_salida, "wb") as f:
        f.write(resultado)

    print(f"Archivo cifrado guardado en: {ruta_salida}")
    return resultado


def descifrar_archivo(ruta_entrada, ruta_salida, llave):
    """Descifra un archivo cifrado."""
    with open(ruta_entrada, "rb") as f:
        datos = f.read()

    texto = descifrar(datos, llave)
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"Archivo descifrado guardado en: {ruta_salida}")
    return texto


def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python encriptador.py generar")
        print("  python encriptador.py cifrar <archivo> <salida>")
        print("  python encriptador.py descifrar <archivo> <salida>")
        return

    comando = sys.argv[1].lower()

    if comando == "generar":
        generar_llave()

    elif comando == "cifrar":
        if len(sys.argv) != 4:
            print("Uso: python encriptador.py cifrar <entrada> <salida>")
            return
        with open("llave.key", "rb") as f:
            llave = f.read()
        cifrar_archivo(sys.argv[2], sys.argv[3], llave)

    elif comando == "descifrar":
        if len(sys.argv) != 4:
            print("Uso: python encriptador.py descifrar <entrada> <salida>")
            return
        with open("llave.key", "rb") as f:
            llave = f.read()
        descifrar_archivo(sys.argv[2], sys.argv[3], llave)

    else:
        print(f"Comando no reconocido: {comando}")


if __name__ == "__main__":
    main()