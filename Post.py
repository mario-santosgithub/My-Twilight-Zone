class Post:

    def __init__(self, user, hashtags, stance, message):
        self.user = user
        self.hashtags = hashtags
        self.stance = stance
        self.message = message
        self.comments = []

    def getUser(self):
        return self.user

    def getHashtags(self):
        return self.hashtags

    def getStance(self):
        return self.stance
        
    def getMessage(self):
        return self.message
    
    def getComments(self):
        return self.comments

    def addComment(self, comment):
        self.comments.append(comment)
