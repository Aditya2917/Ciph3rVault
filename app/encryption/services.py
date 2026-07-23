from crypto.aes import encrypt_aes, decrypt_aes


def process_aes(text, key, operation):

    if operation == "encrypt":
        return encrypt_aes(text, key)

    return decrypt_aes(text, key)