import struct


def main():
    fmt = '<3s3sHH'
    with open('filter.gif', 'rb') as fb:
        img = memoryview(fb.read())
    header = img[:10]
    b = bytes(header)
    print(b)
    s = struct.unpack(fmt, header)
    del header, img


if __name__ == '__main__':
    main()
