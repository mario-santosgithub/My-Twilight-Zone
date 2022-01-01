class User(object):

    def __init__(self, userId, userKind):
        self.userId = userId;
        self.userKind = userKind
        self.friends = []
        self.posts = []
        self.comments = []

    def getId(self):
        return self.userId

    def getUserKind(self):
        return self.userKind

    def getFriends(self):
        return self.friends
    
    def getPosts(self):
        return self.posts

    def getComments(self):
        return self.comments

    def addFriend(self, user):
        self.friends.append(user)

    def addPost(self, post):
        self.posts.append(post)


class Fanatic(User):

    def __init__(self, userId, userKind, lovesHates):
        self.lovesHates = lovesHates
        super().__init__(userId, userKind)

    def getId(self):
        return super().getId()

    def getUserKind(self):
        return super().getUserKind()

    def getFriends(self):
        return super().getFriends()
    
    def getPosts(self):
        return super().getPosts()

    def getComments(self):
        return super().getComments()
    
    def addFriend(self, user):
        return super().addFriend(user)

    def addPost(self, post):
        super().addPost(post)

    def getLovesHates(self):
        return self.lovesHates




class Naive(User):

    def __init__(self, userId, userKind):
        super().__init__(userId, userKind)
    
    def getId(self):
        return super().getId()

    def getUserKind(self):
        return super().getUserKind()

    def getFriends(self):
        return super().getFriends()
    
    def getPosts(self):
        return super().getPosts()

    def getComments(self):
        return super().getComments()

    def addFriend(self, user):
        return super().addFriend(user)

    def addPost(self, post):
        super().addPost(post)
    
class SelfCentered(User):

    def __init__(self, userId, userKind):
        super().__init__(userId, userKind)
    
    def getId(self):
        return super().getId()

    def getUserKind(self):
        return super().getUserKind()

    def getFriends(self):
        return super().getFriends()
    
    def getPosts(self):
        return super().getPosts()

    def getComments(self):
        return super().getComments()

    def addFriend(self, user):
        return super().addFriend(user)

    def addPost(self, post):
        super().addPost(post)
