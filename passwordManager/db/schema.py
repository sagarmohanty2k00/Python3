class StoredPassword:
    def __init__(self, website="", password="", owner=""):
        self.website = website
        self.password = password
        self.owner = owner

    def getter(self):
        return [self.website, self.password]

    def changePassword(self, password):
        self.password = password


class User:
    def __init__(self):
        self.userName = ""
        self.password = ""

    def setter(self, userName, password):
        self.userName = userName
        self.password = password

    def getter(self):
        return [self.userName, self.password]

    def changePassword(self, password):
        self.password = password