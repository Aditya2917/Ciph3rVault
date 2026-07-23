from crypto.aes import encrypt_aes, decrypt_aes


def process_aes(text, key, operation):

    text = text.strip()
    key = key.strip()

    if not text:
        return False, "Please enter some text."

    if len(key) not in [16, 24, 32]:
        return False, "AES key must be exactly 16, 24 or 32 characters."

    try:

        if operation == "encrypt":
            result = encrypt_aes(text, key)
        else:
            result = decrypt_aes(text, key)

        return True, result

    except Exception:

        return False, "Invalid encrypted text or wrong secret key."