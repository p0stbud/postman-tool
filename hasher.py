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
        print('Type, Hash, Path')
        if 'MD4' in namespaces.type:
            [hasher.calc_md4(file) for file in files]
            for h, f in zip(hasher.md4, files):
                print(f"MD4, {h.upper()}, {f}")

        if 'ed2k' in namespaces.type:
            [hasher.calc_ed2k(file) for file in files]
            for h, f in zip(hasher.ed2k, files):
                print(f"ed2k, {h.upper()}, {f}")

        if 'SHA1_base32' in namespaces.type:
            [hasher.calc_sha1_base32(file) for file in files]
            for h, f in zip(hasher.sha1_base32, files):
                print(f"SHA1_base32, {h.upper()}, {f}")

    except FileNotFoundError:
        print(f"Katalog '{path}' nie istnieje.")
    except PermissionError:
        print(f"Brak uprawnień do odczytu katalogu '{path}'.")


class Hasher:
    md4 = []
    ed2k = []
    sha1_base32 = []

    def calc_md4(self, file_path):
        """Oblicza hash MD4 dla pliku."""
        try:
            with open(file_path, "rb") as f:
                chunk = f.read()
                self.md4.append((MD4.new(chunk).digest()).hex())

        except Exception as e:
            print(f"Error: {e}")
            return None

    def calc_ed2k(self, file):
        """Oblicza hash ED2K dla pliku zgodnie ze specyfikacją eDonkey2000."""
        try:
            CHUNK_SIZE = 9728000  # 9.28 MB
            chunks = []

            with open(file, "rb") as f:
                while chunk := f.read(CHUNK_SIZE):
                    chunks.append(MD4.new(chunk).digest())

            if len(chunks) == 1:
                self.ed2k.append(chunks[0].hex())
            else:
                final_md4 = MD4.new()
                for chunk_hash in chunks:
                    final_md4.update(chunk_hash)
                self.ed2k.append(final_md4.hexdigest())

        except Exception as e:
            print(f"Error: {e}")


    def calc_sha1_base32(self, file):
        """Oblicza hash SHA1 zakodowany w base32 dla pliku."""
        try:
            with open(file, "rb") as f:
                sha1 = SHA1.new()
                while chunk := f.read(8192):
                    sha1.update(chunk)
                sha1_base32 = base64.b32encode(sha1.digest()).decode()
                self.sha1_base32.append(sha1_base32)

        except Exception as e:
            return f"Błąd: {e}"
