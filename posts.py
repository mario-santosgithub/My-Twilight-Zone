# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:31:52 2021

@author: Madalena Custódio - 63128, Mariana Pereira - 62968, Rafaela Reis - 63040
"""

class Post:
    def __init__(self, user, hashtags, stance, postId, message):
        self.user = user
        self.hashtags = hashtags
        self.stance = stance
        self.message = message
        self.postId = postId
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

    def getId(self):
        return self.postId

    def addComment(self, comment):
        self.comments.append(comment)

    def getCommentsNumber(self):
        return len(self.comments)