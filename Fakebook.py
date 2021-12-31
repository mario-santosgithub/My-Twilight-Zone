class Fakebook:

    def __init__(self):
        self.users = []
        self.posts = []

    def addUser(self, user):
        self.users.append(user)

    def getUsers(self):
        return self.users

    def addPost(self, post):
        self.posts.append(post)
        
