from Strings import *
from User import *
from Fakebook import *
from Post import *


fakebook = Fakebook()


#Interpretador de comandos
def main():
    line = input()
    arguments = line.split()
    command = arguments[0].upper()

    while command != EXIT:
        if command == HELP:
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
        elif command == REGISTER:
            registerUser(arguments)
        elif command == USERS:
            users(arguments)
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

        else:
            print(MSG_UNKNOW)
        
        line = input()
        arguments = line.split()
        command = arguments[0].upper()
    print(BYE_MSG)
        


def registerUser(arguments):
    global fakebook

    userKind = arguments[1]
    if userKind.upper() not in ["NAIVE", "FANATIC", "SELFCENTERED"]:
        print(userKind.lower() + " is an invalid user kind!")
        return


    userId = ""
    for word in range(2, len(arguments)):
        userId = userId + arguments[word] + " "
    userId = userId[0:-1]

    users = fakebook.getUsers()

    for user in users:
        if userId == user.getId():
            print(userId + " already exists!")
            return



    if userKind.upper() == "FANATIC":
        lovesHates = input()
        lovesHates = lovesHates.split()
        loves = []
        hates = []
        read = "loves"
        for word in lovesHates:
            if word == "loves":
                read = "loves"
            elif word == "hates":
                read = "hates"
            else:
                if read == "loves":
                    loves.append(word)
                else:
                    hates.append(word)

        for i in loves:
            for j in hates:
                if j == i:
                    print("Invalid fanaticism list!")
                    return

        user = Fanatic(userId, userKind, loves, hates)

    elif userKind.upper() == "NAIVE":
        user = Naive(userId, userKind)
    else:
        user = SelfCentered(userId, userKind)

    fakebook.addUser(user)
    print(userId + " registered.")

def users(arguments):
    users = fakebook.getUsers()
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
    for word in range(1, len(arguments)):
        userId1 = userId1 + arguments[word] + " "
    userId1 = userId1[0:-1]

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
        print(userId1 + " must really admire " + userId2)
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
    for word in range(1, len(arguments)):
        userId = userId + arguments[word] + " "
    userId = userId[0:-1]
    exists = False
   
    line = input()
    hashtags = line.split()
    
    
    line = input()
    lastinput = line.split()
    HF = lastinput[0] # honest or fake
    
    message = ""
    for i in range(1, len(lastinput)):
        message = message + lastinput[i] + " "

    message[0:-1]
  
    users = fakebook.getUsers()
    for u in users:
        if userId == u.getId():
            exists = True
            user = u
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
 
    if user.getUserKind().upper() == "FANATIC":
        hates = user.getHates()
        for i in hashtags:
            for j in hates:
                if i == j and HF == "honest":
                    print("Inadequate stance!")
                    return
    
    post = Post(user, hashtags, HF, message)
    fakebook.addPost(post)
    user.addPost(post)
    friends = user.getFriends()
    print(userId + " sent a " + HF + " post to " + str(len(friends)) + " friends. Post id = " + str(len(user.getPosts())))

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
        HF = post.getHF()
        message = post.getMessage()
        numberComments = len(post.getComments())
        
        print("{}. [{}] {}[{} comments]".format(counter, HF, message, numberComments))
         
def comment(arguments):

    userId1 = ""
    for word in range(1, len(arguments)):
        userId1 = userId1 + arguments[word] + " "
    userId1 = userId1[0:-1]
    exists1 = False

    users = fakebook.getUsers()

    for u in users:
        if userId1 == u.getId():
            exists1 = True
            user1 = u

    userId2 = input()
    exists2 = False
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


    




main()
