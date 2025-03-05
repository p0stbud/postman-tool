import os
import base64
from Crypto.Hash import MD4, SHA1


def hasher_tool(namespaces):
    path = namespaces.path
    if not path:
        path = os.getcwd()

    hasher = Hasher()
    files = []
    if os.path.isdir(path):
        files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    elif os.path.isfile(path):
        files.append(path)
    else:
        print("Ścieżka nie istnieje")
        return
    try:
        if 'ed2k' in namespaces.type:
            for file in files:
                hasher.calc_ed2k(file)
            for h in hasher.ed2k:
                print(f"ed2k: {h.upper()}")
        if 'SHA1_base32' in namespaces.type:
            for file in files:
                hasher.calc_sha1_base32(file)
            for h in hasher.sha1_base32:
                print(f"SHA1_base32: {h.upper()}")
    except FileNotFoundError:
        print(f"Katalog '{path}' nie istnieje.")
    except PermissionError:
        print(f"Brak uprawnień do odczytu katalogu '{path}'.")

class Hasher:
    def __init__(self):
        self.ed2k = []
        self.sha1_base32 = []

    def calc_ed2k(self, file):
        try:
            chunk_size = 9728000
            with open(file, "rb") as f:
                chunks = []
                while chunk := f.read(chunk_size):
                    chunk_md4 = MD4.new(chunk).digest()
                    chunks.append(chunk_md4)
                if len(chunks) == 1:
                    self.ed2k.append(chunks[0].hex())
                else:
                    final_md4 = MD4.new()
                    for chunk in chunks:
                        final_md4.update(chunk)
                    self.ed2k.append(final_md4.hexdigest())
        except Exception as e:
            return f"Błąd: {e}"

    def calc_sha1_base32(self, file):
        try:
            with open(file, "rb") as f:
                sha1 = SHA1.new()
                while chunk := f.read(8192):
                    sha1.update(chunk)
                sha1_base32 = base64.b32encode(sha1.digest()).decode()
                self.sha1_base32.append(sha1_base32)
        except Exception as e:
            return f"Błąd: {e}"
