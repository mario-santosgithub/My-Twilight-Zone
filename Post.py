class Post:

    def __init__(self, user, hashtags, HF, message):
        self.user = user
        self.hashtags = hashtags
        self.HF = HF
        self.message = message
        self.comments = []

    def getUser(self):
        return self.user

    def getHashtags(self):
        return self.hashtags

    def getHF(self):
        return self.HF
        
    def getMessage(self):
        return self.message
    
    def getComments(self):
        return self.comments
