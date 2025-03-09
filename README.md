# postman-tool

## POSTMAN-TOOL - Hasher

**hasher** to narzędzie w ramach projektu **POSTMAN-TOOL**, które umożliwia obliczanie hashy dla plików. Obsługiwane są trzy typy hashy: MD4, SHA1 (base32) oraz ed2k.

### Wymagania

- Python 3.x
- Biblioteka pycryptodome do obsługi algorytmu MD4 i SHA1.

### Instalacja

Zainstaluj wymagane biblioteki:

```bash
pip install pycryptodome
```

### Użycie
#### Uruchamianie narzędzia hasher:

Aby uruchomić narzędzie hasher, należy wywołać je z poziomu terminala, wskazując opcjonalnie ścieżkę do plików oraz typy hashy, które chcesz obliczyć. Możesz obliczać jeden lub więcej typów hashy.

#### Składnia:
```bash
python3 postman-tool.py hasher -t <typ_hasha> -p <ścieżka>
```
#### Opcje:

- -t, --type: Określa typ hasha, który ma być obliczony. Wartości do wyboru:
- ed2k – Hash zgodny ze specyfikacją eDonkey2000.
- SHA1_base32 – Hash SHA1 zakodowany w base32.
- MD4 – Hash MD4.
#### Przykład: -t ed2k SHA1_base32.
- -p, --path: Określa ścieżkę do katalogu lub pliku, dla którego mają być obliczone hashe. Jeśli nie podasz tej opcji, - narzędzie spróbuje użyć bieżącego katalogu.

#### Przykłady:

#### - Obliczenie hashów dla pliku file.txt:
```bash
python3 postman-tool.py hasher -t ed2k MD4 -p /path/to/file.txt
```
#### - Obliczenie hashów dla wszystkich plików w katalogu:
```bash
python3 postman-tool.py hasher -t SHA1_base32 -p /path/to/directory
```
#### - Obliczenie domyślnych hashów (ed2k i SHA1_base32) dla pliku w bieżącym katalogu:
```bash
python3 postman-tool.py hasher -p file.txt
```
#### Wydruk wyników:
Po obliczeniu hashów dla plików, narzędzie wypisuje wyniki w następującym formacie:

```php-template
Type, Hash, Path
MD4, <hash>, <file_path>
SHA1_base32, <hash>, <file_path>
ed2k, <hash>, <file_path>
```
#### Przykładowe wyjście:
```pgsql
Type, Hash, Path
MD4, D41D8CD98F00B204E9800998ECF8427E, /path/to/file.txt
SHA1_base32, MFRGGZDFMZTWQ2TLN4ZGLOJ3IFQPE36DQKMLO2DY, /path/to/file.txt
ed2k, 74B87337454200D4D33F80C4663DC5B4, /path/to/file.txt
```
#### Zasady i ograniczenia:
- Narzędzie wspiera tylko lokalne pliki i katalogi.
- Hashowanie działa na plikach o dowolnym rozmiarze, ale należy pamiętać, że obliczanie hashów dla bardzo dużych plików może zająć trochę czasu.

### Podsumowanie:
Narzędzie hasher jest prostym i efektywnym sposobem na generowanie hashy dla plików w różnych formatach (MD4, SHA1_base32, ed2k). Dzięki temu narzędziu możesz łatwo uzyskać unikalne identyfikatory plików, które mogą być użyteczne w przypadku porównań, weryfikacji integralności danych lub innych zadań związanych z bezpieczeństwem.
