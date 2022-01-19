import asyncio
from asyncore import write
from email import message
from urllib import response
from connectionPool import ConnectionPool


async def handle_connection(reader, writer):
    # Get nickname for the newly connected client
    writer.write("> Choose a nickname: ".encode())
    response = await reader.readuntil(b"\n")
    writer.nickname = response.decode().strip()

    connection_pool.add_new_user_to_pool(writer)
    connection_pool.send_welcome_message(writer)
    await writer.drain()

    # Let's run an infinite loop
    while True:
        writer.write(f"> ".encode())
        try:
            data = await reader.readuntil(b"\n")
        except:
            connection_pool.broadcast_user_quit(writer)
            break

        message = data.decode().strip()

        if message == "/list":
            connection_pool.list_users(writer)
        elif message == "/quit":
            connection_pool.broadcast_user_quit(writer)
            break
        else :
            connection_pool.broadcast_new_message(writer, message)

        await writer.drain()

        if writer.is_closing():
            break
    
    # Let's close the connection once we are out of the loop and clean up
    writer.close()
    await writer.wait_closed()
    connection_pool.remove_user_from_pool(writer)

async def main():
    server = await asyncio.start_server(handle_connection, "0.0.0.0", 8000)

    async with server:
        await server.serve_forever()

connection_pool = ConnectionPool()
asyncio.run(main())