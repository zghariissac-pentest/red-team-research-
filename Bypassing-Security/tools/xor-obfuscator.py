import sys

def xor_encode(data: bytes, key: int) -> bytes:
    return bytes([b ^ key for b in data])

def xor_decode(data: bytes, key: int) -> bytes:
    return bytes([b ^ key for b in data])

def main():
    if len(sys.argv) < 4:
        print("Usage:")
        print("  python xor-obfuscator.py [encode|decode] <key:int> <text>")
        return

    mode = sys.argv[1].lower()
    key = int(sys.argv[2])
    text = sys.argv[3].encode()

    if mode == "encode":
        result = xor_encode(text, key)
        print("Encoded:", result.hex())

    elif mode == "decode":
        try:
            decoded = xor_decode(bytes.fromhex(text.decode()), key)
            print("Decoded:", decoded.decode(errors="ignore"))
        except ValueError:
            print("Invalid input format")

    else:
        print("Unknown mode")

if __name__ == "__main__":
    main()

