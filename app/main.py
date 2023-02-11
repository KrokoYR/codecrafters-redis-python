import asyncio

HOST = '0.0.0.0'
PORT = 6379


async def handler(reader, writer):
    while True:
        data = await reader.read(1024)
        if not data:
            break

        writer.write(b"+PONG\r\n")
        await writer.drain()
    writer.close()
    await writer.wait_closed()


async def redis_server():
    server = await asyncio.start_server(
        handler, host=HOST, port=PORT, reuse_port=True
    )
    async with server:
        await server.serve_forever()


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    asyncio.run(redis_server())


if __name__ == "__main__":
    main()
