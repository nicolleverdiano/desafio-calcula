def calcula_hash(palavra):
    return sum(ord(letra) for letra in palavra)

palavra1 = "amor"
palavra2 = "roma"

hash1 = calcula_hash(palavra1)
hash2 = calcula_hash(palavra2)

print(f"Palavra 1: '{palavra1}' -> Hash: {hash1}")
print(f"Palavra 2: '{palavra2}' -> Hash: {hash2}")

if palavra1 != palavra2 and hash1 == hash2:
    print("\n[Sucesso] Duas palavras diferentes geraram o mesmo valor de hash!")