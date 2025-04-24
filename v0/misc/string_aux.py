def encode_string(s: str) -> int:
    return sum(ord(char) * (256 ** i) for i, char in enumerate(s))

def decode_string(n: int) -> str:
    chars = []
    while n > 0:
        chars.append(chr(n % 256))
        n //= 256
    return ''.join(chars)