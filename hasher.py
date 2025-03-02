import os
from Crypto.Hash import MD4


def _hasher():
    pass


def ed2k_hash(file_path=os.getcwd()):
    try:
        chunk_size = 9728000  # 9.28 MB

        with open(file_path, "rb") as f:
            chunks = []
            while chunk := f.read(chunk_size):
                chunk_md4 = MD4.new(chunk).digest()
                chunks.append(chunk_md4)

        if len(chunks) == 1:
            return chunks[0].hex()
        else:
            final_md4 = MD4.new()
            for chunk in chunks:
                final_md4.update(chunk)
            return final_md4.hexdigest()
    except Exception as e:
        return f"Błąd: {e}"