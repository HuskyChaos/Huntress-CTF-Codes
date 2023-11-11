# Not my code
# Thanks to a friend for this one. Check out his writeups as well to see more ways to solve challenges.
# https://github.com/s7otbxdx/huntress-ctf-2023

#!/usr/bin/env python3
import sys

def xor_strings(string_1: str, string_2: str) -> str:
    result = ''
    for i in range(len(string_1)):
        result += chr(ord(string_1[i]) ^ ord(string_2[i % len(string_2)]))
    return result

# driver code
if __name__ == '__main__':
    try:
        plaintext = 'THE TRAGEDY OF HAMLET, PRINCE OF DENMARK'
        ciphertext = '''7'6M;0..&+*M $O!""?(;NO91&=.*B /C+6#"#="iey^O^VB8^@^O^C^Z^L^BB<^A^B^D^V^^^_^G^N^[^Feyge&^]^H^N^N^G>^GAO^Q^@^GC^[^\M^['''
        key = xor_strings(plaintext, ciphertext)[:16]
        print(key)
        sys.exit(0)
    except Exception as err:
        print(err)
        sys.exit(1)
