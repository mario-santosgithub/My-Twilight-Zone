from Strings import *
from User import *
from Fakebook import *
from Post import *
from Comment import *
import operator

fakebook = Fakebook()

def main():
    line = input()
    arguments = line.split()
    command = arguments[0].upper()

    while command != EXIT:
        if command == HELP:
            help()
        elif command == REGISTER:
            registerUser(arguments)
        elif command == USERS:
            users()
        elif command == ADDFRIEND:
            addFriend(arguments)
        elif command == FRIENDS:
            friends(arguments)
        elif command == POST:
            post(arguments)
        elif command == USERPOSTS:
            userPosts(arguments)
        elif command == COMMENT:
            comment(arguments)
        elif command == READPOST:
            readPost(arguments)

        else:
            print(MSG_UNKNOWN)


        line = input()
        arguments = line.split()
        command = arguments[0].upper()

    print(BYE_MSG)

def help():
    print(REGISTER.lower() + " - " + MSG_REGISTER)
    print(ADDFRIEND.lower() + " - " + MSG_ADDFRIEND)
    print(FRIENDS.lower() + " - " + MSG_FRIENDS)
    print(POST.lower() + " - " + MSG_POST)
    print(USERPOSTS.lower() + " - " + MSG_USERPOSTS)
    print(COMMENT.lower() + " - " + MSG_COMMENT)
    print(READPOST.lower() + " - " + MSG_READPOST)
    print(COMMENTSBYUSER.lower() + " - " + MSG_COMMENTSBYUSER)
    print(TOPICFANATICS.lower() + " - " + MSG_TOPICFANATICS)
    print(TOPICPOSTS.lower() + " - " + MSG_TOPICPOSTS)
    print(HELP.lower() + " - " + MSG_HELP)
    print(EXIT.lower() + " - " + MSG_EXIT)

def registerUser(arguments):

    userKind = arguments[1]
    if userKind.upper() not in ["NAIVE", "FANATIC", "SELFCENTERED"]:
        print(userKind.lower() + " is an invalid user kind!")
        return
    
    userId = ""
    for i in range(2, len(arguments)):
        userId += arguments[i] + " "
    userId = userId[0:-1]

    users = fakebook.getUsers()

    for user in users:
        if userId == user.getId():
            print(userId + " already exists!")
            return
    
    if userKind.upper() == "FANATIC":
        hashtags = input().split()
        lovesHates = []
        loves = []
        hates = []
        read = "LOVES"
        for word in hashtags:
            if word.upper() == "LOVES":
                read = "LOVES"
            elif word.upper() == "HATES":
                read = "HATES"
            else:
                lovesHates.append([read, word])
                if read.upper() == "LOVES":
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

        user = Fanatic(userId, userKind, lovesHates)

    elif userKind.upper() == "NAIVE":
        user = Naive(userId, userKind)
    else:
        user = SelfCentered(userId, userKind)

    fakebook.addUser(user)
    print(userId + " registered.")

def users():
    users = fakebook.getUsers()
    users.sort(key=operator.attrgetter("userId"))
    if users == []:
        print("There are no users!")
        return
    else:
        for user in users:
            userId = user.getId()
            userKind = user.getUserKind()
            friendsCount = len(user.getFriends())
            postsCount = len(user.getPosts())
            commentsCount = len(user.getComments())

            print("{} [{}] {} {} {}".format(userId, userKind, friendsCount, postsCount, commentsCount))

    return

def addFriend(arguments):
    users = fakebook.getUsers()
    
    userId1 = ""
    for i in range(1, len(arguments)):
        userId1 = userId1 + arguments[i] + " "
    userId1 = userId1[:-1]
    exists1 = False

    userId2 = input()
    exists2 = False

    for user in users:
        if userId1 == user.getId():
            exists1 = True
            user1 = user
    for user in users:
        if userId2 == user.getId():
            exists2 = True
            user2 = user

    if exists1 == False:
        print(userId1 + " does not exist!")
        return
    if exists2 == False:
        print(userId2 + " does not exist!")
        return
    if userId1 == userId2:
        print(userId1 + " cannot be the same as " + userId2 + "!")
        return
    if user1 in user2.getFriends():
        print(userId1 + " must really admire " + userId2+ "!")
        return

    user1.addFriend(user2)
    user2.addFriend(user1)
    print(userId1 + " is friend of " + userId2 + ".")
    return

def friends(arguments):
    userId = ""
    for word in range(1, len(arguments)):
        userId = userId + arguments[word] + " "
    userId = userId[0:-1]
    exists = False

    users = fakebook.getUsers()

    for u in users:
        if userId == u.getId():
            exists = True
            user = u

    if exists == False:
        print(userId + " does not exist!")
        return

    if len(user.getFriends()) == 0:
        print(userId + " has no friends!")
        return

    string = ""
    friends = user.getFriends()
    for u in friends:
        string = string + u.getId() + ", "

    string = string[0:-2]
    print(string + ".")

def post(arguments):

    userId = ""
    for i in range(1, len(arguments)):
        userId += arguments[i] + " "
    userId = userId[:-1]
    exists = False

    users = fakebook.getUsers()

    for u in users:
        if userId == u.getId():
            user = u
            exists = True


    hashtags = input().split()
    lastInput = input().split()
    stance = lastInput[0]

    message = ""
    for i in range(1, len(lastInput)):
        message += lastInput[i] + " "
    message = message[:-1]

    if exists == False:
        print(userId + " does not exist!")
        return

    if hashtags == []:
        print("Invalid hashtags list!")
        return
    for h in hashtags:
        counter = 0
        for h2 in hashtags:
            if h == h2:
                counter = counter + 1
        if counter > 1:
            print("Invalid hashtags list!")
            return

    if user.getUserKind().upper() == "FANATIC" and stance.upper() == "HONEST":
        lovesHates = user.getLovesHates()
        for entry in lovesHates:
            if entry[0] == "HATES" and entry[1] in hashtags:
                print("inadequate stance!")
                return
    
    post = Post(user, hashtags, stance, message)
    fakebook.addPost(post)
    user.addPost(post)
    friends = user.getFriends()
    print(userId + " sent a " + stance + " post to " + str(len(friends)) + " friends. Post id = " + str(len(user.getPosts())) + ".")

def userPosts(arguments):

    userId = ""
    for word in range(1, len(arguments)):
        userId = userId + arguments[word] + " "
    userId = userId[0:-1]
    exists = False

    users = fakebook.getUsers()

    for u in users:
        if userId == u.getId():
            exists = True
            user = u

    if exists == False:
        print(userId + " does not exist!")
        return

    posts = user.getPosts()
    if posts == []:
        print(userId + " has no posts!")
        return

    counter = 1
    print(userId + " posts:")
    for post in posts:
        stance = post.getStance()
        message = post.getMessage()
        numberComments = len(post.getComments())
        
        print("{}. [{}] {} [{} comments]".format(counter, stance, message, numberComments))

def comment(arguments):

    userId1 = ""
    for word in range(1, len(arguments)):
        userId1 += arguments[word] + " "
    userId1 = userId1[0:-1]
    exists1 = False

    userId2 = input()
    exists2 = False

    lastInput = input().split()

    postId = int(lastInput[0])
    commentStance = lastInput[1]

    message = ""
    for word in range(2, len(lastInput)):
        message += lastInput[word] + " "
    message = message[0:-1]

    users = fakebook.getUsers()
    for u in users:
        if userId1 == u.getId():
            exists1 = True
            user1 = u

    for u in users:
        if userId2 == u.getId():
            exists2 = True
            user2 = u

    if exists1 == False:
        print(userId1 + " does not exist!")
        return
    if exists2 == False:
        print(userId2 + " does not exist!")
        return

    postList = user2.getPosts()

    if postId > len(postList):
        print("{} has no post {}!".format(userId2, postId))
        return

    post = postList[postId-1]


    hasAccess = False
    friends2 = user2.getFriends()
    friends2.append(user2) # o user2 pode comentar no seu proprio post
    for u in friends2:
        if user1 == u:
            hasAccess = True

    if hasAccess == False:
        print("{} has no access to post {} by {}!".format(userId1, postId, userId2))
        return 

    if user1.getUserKind().upper() == "SELFCENTERED" and user1 != user2:
        print(userId1 + " cannot comment on this post!")
        return
    
    postStance = post.getStance()
    postHashTags = post.getHashtags()

    if user1.getUserKind().upper() == "FANATIC":
        lovesHates = user1.getLovesHates()
        for h in postHashTags:
            for entry in lovesHates:
                if h == entry[1] and entry[0].upper() == "LOVES":
                    fanaticism = 1 # positive
                    break
                elif h == entry[1] and entry[0].upper() == "HATES":
                    fanaticism = 0 #negative
                    break
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

def readPost(arguments):

    userId = ""
    for i in range(1, len(arguments)):
        userId += arguments[i] + " "
    userId = userId[:-1]
    exists = False

    users = fakebook.getUsers()
    for u in users:
        if userId == u.getId():
            user = u
            exists = True

    postId = int(input())
    posts = user.getPosts()

    if exists == False:
        print(userId + " does not exist!")
        return
    if postId > len(posts):
        print(userId+ "has no post " + postId + "!")
        return

    post = posts[postId-1]
    
    message = post.getMessage()
    comments = post.getComments()
    print("[{}] {}".format(userId, message))

    if comments == []:
        print("No comments!")
        return

    for comment in comments:
        userc = comment.getUser()
        userIdc = userc.getId()
        messagec = comment.getMessage()
        print("[{}] {}".format(userIdc, messagec))

main()
