def cifra_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            deslocamento_mod = deslocamento % 26
            start = ord('A') if char.isupper() else ord('a')
            resultado += chr(start + (ord(char) - start + deslocamento_mod) % 26)
        else:
            resultado += char
    return resultado

def decifra_cesar(texto, deslocamento):
    return cifra_cesar(texto, -deslocamento)

# Exemplo de uso:

#texto_original = input()
texto_original = "Eu sou o caminho, a verdade e a vida (Jesus)"
deslocamento = 3

texto_criptografado = cifra_cesar(texto_original, deslocamento)
print("Texto Criptografado:", texto_criptografado)

texto_descriptografado = decifra_cesar(texto_criptografado, deslocamento)
print("Texto Descriptografado:", texto_descriptografado)