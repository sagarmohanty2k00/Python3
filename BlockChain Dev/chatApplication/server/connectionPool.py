import asyncio
from asyncore import write
from textwrap import dedent


class ConnectionPool:
    def __init__(self):
        self.connection_pool = set()

    def send_welcome_message(self, writer):
        """
        Sends welcome message to newly connected client
        """
        message = dedent(f"""
        ===
        Welcome {writer.nickname}!

        There are {len(self.connection_pool) - 1} users(s) here beside you

        Help:

        - Type anything to chat
        - /list will list all the connected users
        - /quit will disconnect you
        ===
        """)
        writer.write(f"{message}\n".encode())

    def broadcast(self, writer, message):
        """
        Broadcasts a general message to the entire pool
        """
        for user in self.connection_pool:
            if user == writer:
                continue

            user.write(f"{message}\n".encode())

    def broadcast_user_join(self, writer):
        """
        Calls the broadcast method with a "user joining" message
        """
        self.broadcast(writer, f"{writer.nickname} just joined")

    def broadcast_user_quit(self, writer):
        """
        Calls the broadcast method with a "user quiting" message
        """
        self.broadcast(writer, f"{writer.nickname} just quit")

    def broadcast_new_message(self, writer, message):
        """
        Calls the broadcast method with a user's chat message
        """
        self.broadcast(writer, f"[{writer.nickname}] {message}")

    def list_users(self, writer):
        """
        Lists all users in the pool
        """
        message = "===\n"
        message += "Currently connected users:"

        for user in self.connection_pool:
            if user == writer:
                message += f"\n - {user.nickname} (you)"
            else:
                message += f"\n - {user.nickname}"
        
        writer.write(f"{message}\n".encode())

    def add_new_user_to_pool(self, writer):
        """
        Adds new users to our existing pool
        """
        self.connection_pool.add(writer)

    def remove_user_from_pool(self, writer):
        """
        Removes an existing user from the  pool
        """
        self.connection_pool.remove(writer)