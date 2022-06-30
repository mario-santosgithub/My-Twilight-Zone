# -*- coding: utf-8 -*-

#Comandos
EXIT = "exit"
HELP = "help"
REGISTER = "register"
USERS = "users"
ADDFRIEND = "addfriend"
FRIENDS = "friends"
POST = "post"
USERPOSTS = "userposts"
COMMENT = "comment"
READPOST = "readpost"
COMMENTSBYUSER = "commentsbyuser"
TOPICFANATICS = "topicfanatics"
TOPICPOSTS = "topicposts"

#Mensagens dos comandos 
MSG_REGISTER = "registers a new user"
MSG_USERS = "lists all users"
MSG_ADDFRIEND = "adds a new friend"
MSG_FRIENDS = "lists the user friends"
MSG_POST = "posts a new message"
MSG_USERPOSTS = "lists all posts by a user"
MSG_COMMENT = "user comments on a post"
MSG_READPOST = "prints detailed info on a post"
MSG_COMMENTSBYUSER = "shows all the comments by a user on a given post"
MSG_TOPICFANATICS = "shows a list of fanatic users on a topic"
MSG_TOPICPOSTS = "shows a list of posts on a given topic"
MSG_HELP = "shows the available commands"
MSG_EXIT = "terminates the execution of the program"
MSG_UNKNOWN = "Unknown command. Type help to see available commands."
BYE_MSG = "Bye!"



from fakebook import Fakebook
import time

def next_command():
    user_input = input().split(" ")
    command = user_input[0].lower()
    args = user_input[1:]
    return command, args
      
def help():
    print(REGISTER.lower() + " - " + MSG_REGISTER)
    print(USERS.lower() + " - " + MSG_USERS)
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
    
def register_user_io(fakebook, args):
    type_user = args[0]
    if type_user not in ["naive", "fanatic", "selfcentered"]:
        print(type_user.lower() + " is an invalid user kind!")
    else:
        fakebook.register_user(args)
        
def users_io(fakebook):
    fakebook.showUsers()
    
def add_friend_io(fakebook, args):
    fakebook.add_friend(args)

def friends_io(fakebook, args):
    fakebook.showFriends(args)
    
def post_io(fakebook, args):
    fakebook.post(args)
    
def user_posts_io(fakebook, args):
    fakebook.userPosts(args)
    
def comment_io(fakebook, args):
    fakebook.commentPost(args)
    
def read_post_io(fakebook, args):
    fakebook.readPost(args)

def comments_by_user_io(fakebook, args):
    fakebook.commentsByUser(args)

def topic_fanatic_io(fakebook, args):
    fakebook.topicFanatic(args)

def topic_posts_io(fakebook, args):
    fakebook.topicPosts(args)
    

       





#Interpretador de comandos
def main():
    time.sleep(20)
    fakebook = Fakebook()
    command, args = next_command()
    
    while command != EXIT:
        if command == HELP:
            help()
        elif command == REGISTER:
            register_user_io(fakebook, args)
        elif command == USERS:
            users_io(fakebook)
        elif command == ADDFRIEND:
            add_friend_io(fakebook, args)
        elif command == FRIENDS:
            friends_io(fakebook, args)
        elif command == POST:
            post_io(fakebook, args)
        elif command == USERPOSTS:
            user_posts_io(fakebook, args)
        elif command == COMMENT:
            comment_io(fakebook, args)
        elif command == READPOST:
            read_post_io(fakebook, args)
        elif command == COMMENTSBYUSER:
            comments_by_user_io(fakebook, args)
        elif command == TOPICFANATICS:
            topic_fanatic_io(fakebook, args)
        elif command == TOPICPOSTS:
            topic_posts_io(fakebook, args)
        else:
            print(MSG_UNKNOWN)
            
        command, args = next_command()

    print(BYE_MSG)
            
            
main()
