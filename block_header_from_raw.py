import json
import struct
import time
import requests


public_node = "https://blockstream.info/api/block/"

def get_raw_block_data(block_hash):
    url = f"{public_node}/{block_hash}/raw"
    response = requests.get(url, stream=True)

    raw_block = response.content

    return raw_block


def parse_block_header(raw_header):
    # 4 bytes for the version (L) L' is for unsigned long
    # 32 bytes for the previous block hash (32s) 32-byte string
    # 32 bytes for the Merkle root (32s)
    # 4 bytes for the timestamp (L)
    # 4 bytes for the bits (L)
    # 4 bytes for the nonce (L)
    header = struct.unpack('<L32s32sLLL', raw_header)

    # Convert the version from little-endian to int
    version = f"0x{header[0]:08x}"

    # Convert the previous block hash and merkle root from little-endian to big-endian and then to a hex string
    previous_block_hash = header[1][::-1].hex()
    merkle_root = header[2][::-1].hex()

    # Convert the timestamp to a human-readable format
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(header[3]))

    # The 'bits' and 'nonce' are already in the correct format, just need to be assigned
    bits = header[4]
    nonce = f"0x{header[5]:08x}"

    # Return the parsed data as a dictionary
    return {
        'version': version,
        'previous_block_hash': previous_block_hash,
        'merkle_root': merkle_root,
        'timestamp': timestamp,
        'bits': bits,
        'difficulty': difficulty(bits),
        'nonce': nonce
    }

# I stole this from StackOver Flow
def nbits(bits):
    hexstr = format(bits, 'x')
    first_byte, last_bytes = hexstr[0:2], hexstr[2:]
    first, last = int(first_byte, 16), int(last_bytes, 16)
    return last * 256 ** (first - 3)

# I stole this from StackOver Flow
def difficulty(bits):
    return 0x00ffff0000000000000000000000000000000000000000000000000000 / nbits(bits)

if __name__ == "__main__":
    block_hash = '00000000000000000002ad3eedeecdad5ab16718b312d640f88c28c59799480b'
    raw_block_data = get_raw_block_data(block_hash)
    block_header_data = parse_block_header(raw_block_data[:80])
    print(json.dumps(block_header_data, indent=4))
