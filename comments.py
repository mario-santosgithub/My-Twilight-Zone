class Comment:
    def __init__(self, user, stance, message):
        self.user = user
        self.stance = stance
        self.message = message

    def getUser(self):
        return self.user

    def getStance(self):
        return self.stance

    def getMessage(self):
        return self.message
