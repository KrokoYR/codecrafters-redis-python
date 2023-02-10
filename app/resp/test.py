CRLF = '\r\n'
test_str = '*2\r\n*3\r\n:1\r\n:2\r\n:3\r\n*2\r\n+Hello\r\n-World\r\n'


def parse_array(chunks: list, length: int, res: list):
    if length == 0:
        return res

    return res


def parse(input_str: str):
    if input_str.startswith('*'):
        chunks = input_str.split(CRLF)
        length = int(chunks[0][1:])
        return parse_array(chunks[1:], length, [])
    else:
        return ''


def main():
    return parse(test_str)


print(main())
