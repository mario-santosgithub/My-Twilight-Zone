from Strings import *
from User import *
from Post import *
from Comment import *
import operator


class Fakebook:

    def __init__(self):
        self.users = []
        self.posts = []


    def register_user(self, args):
            type_user = args[0]
            user_name = ' '.join(args[1:])
            
            hashtags = []
            if type_user == "fanatic":
                hashtags = input().split()

            for user in self.users:
                if user_name == user.getUserName():
                    print(user_name + " already exists!")
                    return

            if type_user == "fanatic":
                lovesHates = []
                loves = []
                hates = []
                read = "loves"
                for word in hashtags:
                    if word == "loves":
                        read = "loves"
                    elif word == "hates":
                        read = "hates"
                    else:
                        lovesHates.append([read, word])
                        if read == "loves":
                            if word in loves:
                                print("Invalid fanaticism list!")
                                return
                            loves.append(word)
                        else:
                            if word in hates:
                                print("Invalid fanaticism list!")
                                return
                            hates.append(word)

                for i in loves:
                    for j in hates:
                        if i == j:
                            print("Invalid fanaticism list!")
                            return
                
                user = Fanatic(user_name, type_user, lovesHates)

            elif type_user == "naive":
                user = Naive(user_name, type_user)
            else:
                user = SelfCentered(user_name, type_user)

            self.users.append(user)
            print(user_name + " registered.")

    def showUsers(self):
        self.users.sort(key=operator.attrgetter("user_name"))

        if self.users == []:
            print("There are no users!")
            return
        else:
            for user in self.users:
                user_name = user.getUserName()
                type_user = user.getTypeUser()
                friendsCount = len(user.getFriends())
                postsCount = len(user.getPosts())
                commentsCount = len(user.getComments())

                print("{} [{}] {} {} {}".format(user_name, type_user, friendsCount, postsCount, commentsCount))

    def add_friend(self, args):

        user_name1 = ' '.join(args)
        exists1 = False

        user_name2 = input()
        exists2 = False

        for user in self.users:
            if user_name1 == user.getUserName():
                exists1 = True
                user1 = user
            if user_name2 == user.getUserName():
                exists2 = True
                user2 = user

        if exists1 == False:
            print(user_name1 + " does not exist!")
            return
        if exists2 == False:
            print(user_name2 + " does not exist!")
            return
        if user_name1 == user_name2:
            print(user_name1 + " cannot be the same as " + user_name2 + "!")
            return
        if user1 in user2.getFriends():
            print(user_name1 + " must really admire " + user_name2 + "!")
            return

        user1.addFriend(user2)
        user2.addFriend(user1)
        print(user_name1 + " is friend of " + user_name2 + ".")
        return

    def showFriends(self, args):
        
        user_name = ' '.join(args)
        exists = False

        for u in self.users:
            if user_name == u.getUserName():
                exists = True
                user = u

        if exists == False:
            print(user_name + " does not exist!")
            return

        if len(user.getFriends()) == 0:
            print(user_name + " has no friends!")
            return

        friends = user.getFriends()
        friends.sort(key=operator.attrgetter("user_name"))
        string = ""
        for u in friends:
            string += u.getUserName() + ", "
        string = string[:-2]
        print(string + ".")


    def post(self, args):
        user_name = ' '.join(args)
        exists = False

        for u in self.users:
            if user_name == u.getUserName():
                user = u
                exists = True

        hashtags = input().split()
        lastInput = input().split()
        stance = lastInput[0]

        message = ' '.join(lastInput[1:])

        if exists == False:
            print(user_name + " does not exist!")
            return

        if hashtags == []:
            print("Invalid hashtags list!")
            return
        for h in hashtags:
            counter = 0
            for h2 in hashtags:
                if h == h2:
                    counter += 1
            if counter > 1:
                print("Invalid hashtags list!")
                return
        
        if user.getTypeUser() == "fanatic" and stance == "honest":
            lovesHates = user.getLovesHates()
            for entry in lovesHates:
                if entry[0] == "hates" and entry[1] in hashtags:
                    print("Inadequate stance!")
                    return

        if user.getTypeUser() == "fanatic" and stance == "fake":
            lovesHates = user.getLovesHates()
            for entry in lovesHates:
                if entry[0] == "loves" and entry[1] in hashtags:
                    print("Inadequate stance!")
                    return

        postId = len(user.getPosts()) + 1
        post = Post(user, hashtags, stance, postId, message)
        self.posts.append(post)
        user.addPost(post)
        friends = user.getFriends()
        print(user_name + " sent a " + stance + " post to " + str(len(friends)) + " friends. Post id = " + str(len(user.getPosts())) + ".")


    def userPosts(self, args):

        user_name = ' '.join(args)
        exists = False

        for u in self.users:
            if user_name == u.getUserName():
                exists = True
                user = u

        if exists == False:
            print(user_name + " does not exist!")
            return
        
        posts = user.getPosts()
        if posts == []:
            print(user_name + " has no posts!")
            return

        counter = 1
        print(user_name + " posts: ")
        for post in posts:
            stance = post.getStance()
            message = post.getMessage()
            numberComments = len(post.getComments())

            print("{}. [{}] {} [{} comments]".format(counter, stance, message, numberComments))
            counter += 1

    def commentPost(self, args):
        user_name1 = ' '.join(args)
        exists1 = False

        user_name2 = input()
        exists2 = False

        lastInput = input().split()
        postId = int(lastInput[0])
        commentStance = lastInput[1]

        message = ' '.join(lastInput[2:])

        for u in self.users:
            if user_name1 == u.getUserName():
                exists1 = True
                user1 = u
            if user_name2 == u.getUserName():
                exists2 = True
                user2 = u

        if exists1 == False:
            print(user_name1 + " does not exist!")
            return
        if exists2 == False:
            print(user_name2 + " does not exist!")
            return

        postList = user2.getPosts()

        if postId > len(postList):
            print("{} has no post {}!".format(user_name2, postId))
            return

        post = postList[postId-1]

        hasAccess = False
        friends2 = user2.getFriends()

        if user1 == user2:
            hasAccess = True

        for u in friends2:
            if user1 == u:
                hasAccess = True

        if hasAccess == False:
            print("{} has no access to post {} by {}!".format(user_name1, postId, user_name2))
            return

        if user1.getTypeUser() == "selfcentered" and user1 != user2:
            print(user_name1 + " cannot comment on this post!")
            return

        postStance = post.getStance()
        postHashTags = post.getHashtags()

        if user1.getTypeUser() == "fanatic":
            fanaticism = None
            lovesHates = user1.getLovesHates()
            for h in postHashTags:
                for entry in lovesHates:
                    if h == entry[1] and entry[0] == "loves":
                        fanaticism = 1 #positive
                        break
                    elif h == entry[1] and entry[0] == "hates":
                        fanaticism = 0 #negative
                        break
                if fanaticism != None:
                    break

            if (fanaticism == 1 and commentStance == "positive") or (fanaticism == 0 and commentStance == "negative"):
                if postStance == "honest":
                    canComment = True
                else:
                    canComment = False
            elif (fanaticism == 0 and postStance == "fake") or (fanaticism == 1 and postStance == "honest"):
                if commentStance == "positive":
                    canComment = True
                else:
                    canComment = False
            else:
                if fanaticism == 1:
                    canComment = True
                else:
                    canComment = False

            if canComment == False:
                print("Invalid comment stance!")
                return
        
        comment = Comment(user1, commentStance, message)
        post.addComment(comment)
        user1.addComment(comment)
        print("Comment added!")

    
    def readPost(self, args):
        user_name = ' '.join(args)
        exists = False

        postIdStr = input()

        for u in self.users:
            if user_name == u.getUserName():
                user = u
                exists = True

        if exists == False:
            print(user_name + " does not exist!")
            return

        
        postId = int(postIdStr)
        posts = user.getPosts()

        if postId > len(posts) or postId <= 0:
            print(user_name + " has no post " + postIdStr + "!")
            return

        post = posts[postId-1]

        message = post.getMessage()
        comments = post.getComments()
        postStance = post.getStance()
        print("[{} {}] {}".format(user_name, postStance, message))

        if comments == []:
            print("No comments!")
            return

        for comment in comments:
            userc = comment.getUser()
            commentStance = comment.getStance()
            user_name_c = userc.getUserName()
            messagec = comment.getMessage()
            print("[{} {}] {}".format(user_name_c, commentStance, messagec))

    def commentsByUser(self, args):

        user_name = ' '.join(args)
        exists = False
        topicId = input()

        for u in self.users:
            if user_name == u.getUserName():
                user = u
                exists = True

        if exists == False:
            print(user_name + " does not exist!")
            return

        userComments = user.getComments()

        if userComments == []:
            print("No comments!")
            return

        counter = 0
        for comment in userComments:
            for post in self.posts:
                if comment in post.getComments() and topicId in post.getHashtags():
                    counter +=1
                    postAuthor = post.getUser()
                    author_name = postAuthor.getUserName()
                    postStance = post.getStance()
                    postId = post.getId()

                    print("[{} {} {} {}] {}".format(author_name, postStance, postId, comment.getStance(), comment.getMessage()))

        if counter == 0:
            print("No comments!")
            return



    def topicFanatic(self, args):
        topic = args[0]

        fanatics = []
        for user in self.users:
            if user.getTypeUser() == "fanatic":
                lovesHates = user.getLovesHates()
                for entry in lovesHates:
                    if entry[1] == topic:
                        fanatics.append(user.getUserName())

        fanatics.sort()
        if fanatics == []:
            print("Oh please, who would be a fanatic of " + topic + "?")
            return

        print(', '.join(fanatics) + ".")


    def topicPosts(self, args):
        topic = args[0]

        posts = []
        for post in self.posts:
            hashtags = post.getHashtags()
            if topic in hashtags:
                posts.append(post)

        if posts == []:
            print("Oh please, who would write about " + topic + "?")
            return


        for post in posts:
            user = post.getUser()
            user_name = user.getUserName()
            postId = post.getId()
            comments = len(post.getComments())
            message = post.getMessage()

            print("{} {} {}: {}".format(user_name, postId, comments, message))


    def addUser(self, user):
        self.users.append(user)

    def getUsers(self):
        return self.users

    def addPost(self, post):
        self.posts.append(post)
