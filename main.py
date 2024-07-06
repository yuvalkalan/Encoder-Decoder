from hashlib import sha512 as hash512


def byte_xor(msg: bytes, key: bytes) -> bytes:
    key_extension = ((key[i % len(key)] + i) % 256 for i in range(len(msg) - len(key)))
    key += bytes(key_extension)
    return bytes([a ^ b for a, b in zip(key, msg)])


def decoder_encoder(src_file, dst_file):
    password = hash512(input('enter password: ').encode()).digest()
    with open(src_file, 'rb') as script_file:
        new_file = byte_xor(script_file.read(), password)
    with open(dst_file, 'w+b') as script_file:
        script_file.write(new_file)


def main():
    src_file = dst_file = None
    while src_file is None or dst_file is None:
        try:
            src_file, dst_file = input('command: ').split('->', maxsplit=1)
            src_file = src_file.strip()
            dst_file = dst_file.strip()
        except ValueError:
            print('Error! please try again!')

    try:
        decoder_encoder(src_file, dst_file)
    except IOError:
        print('Error! please try again!')
        main()


if __name__ == '__main__':
    byte_xor(b'a', b'b')
    main()
