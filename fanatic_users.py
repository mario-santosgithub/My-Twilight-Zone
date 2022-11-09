class Fanatic_user:
    def __init__(self, user_name, type_user, lovesHates):
        self.user_name = user_name
        self.type_user = type_user
        self.friends = []
        self.posts = []
        self.comments = []
        self.lovesHates = lovesHates


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
        
    def getLovesHates(self):
        return self.lovesHates
    
