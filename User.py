class User(object):

    def __init__(self, user_name, type_user):
        self.user_name = user_name
        self.type_user = type_user
        self.friends = []
        self.posts = []
        self.comments = []


    def getUserName(self):
        return self.user_name

    def getTypeUser(self):
        return self.type_user

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

    def addComment(self, comment):
        self.comments.append(comment)



class Fanatic(User):

    def __init__(self, user_name, type_user, lovesHates):
        self.lovesHates = lovesHates
        super().__init__(user_name, type_user)

    def getUserName(self):
        return super().getUserName()

    def getTypeUser(self):
        return super().getTypeUser()

    def getFriends(self):
        return super().getFriends()

    def getPosts(self):
        return super().getPosts()

    def getLovesHates(self):
        return self.lovesHates

    def getComments(self):
        return super().getComments()
        
    def addFriend(self, user):
        return super().addFriend(user)

    def addPost(self, post):
        return super().addPost(post)

    def addComment(self, comment):
        return super().addComment(comment)




class Naive(User):

    def __init__(self, userId, userKind):
        super().__init__(userId, userKind)
    
    def getId(self):
        return super().getId()

    def getTypeUser(self):
        return super().getTypeUser()

    def getFriends(self):
        return super().getFriends()

    def getPosts(self):
        return super().getPosts()

    def getComments(self):
        return super().getComments()

    def addFriend(self, user):
        return super().addFriend(user)

    def addPost(self, post):
        return super().addPost(post)

    def addComment(self, comment):
        return super().addComment(comment)


class SelfCentered(User):

    def __init__(self, userId, userKind):
        super().__init__(userId, userKind)
    
    def getId(self):
        return super().getId()

    def getTypeUser(self):
        return super().getTypeUser()

    def getFriends(self):
        return super().getFriends()

    def getPosts(self):
        return super().getPosts()

    def getComments(self):
        return super().getComments()

    def addFriend(self, user):
        return super().addFriend(user)

    def addPost(self, post):
        return super().addPost(post)

    def addComment(self, comment):
        return super().addComment(comment)
