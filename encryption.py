class EncryptionModule:
    def hash_string(self, input_string):
        import hashlib
        return hashlib.sha256(input_string.encode()).hexdigest()