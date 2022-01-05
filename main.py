from Fakebook import *

import time
def main():
    fakebook = Fakebook()
    command, arguments = next_command()
    
    while command != EXIT:
        if command == HELP:
            help()
        elif command == REGISTER:
            register_user_io(fakebook, arguments)
        elif command == USERS:
            users_io(fakebook)
        elif command == ADDFRIEND:
            add_friend_io(fakebook, arguments)
        elif command == FRIENDS:
            friends_io(fakebook, arguments)
        elif command == POST:
            post_io(fakebook, arguments)
        elif command == USERPOSTS:
            user_posts_io(fakebook, arguments)
        elif command == COMMENT:
            comment_io(fakebook, arguments)
        elif command == READPOST:
            read_post_io(fakebook, arguments)
        elif command == COMMENTSBYUSER:
            comments_by_user_io(fakebook, arguments)
        elif command == TOPICFANATICS:
            topic_fanatic_io(fakebook, arguments)
        elif command == TOPICPOSTS:
            topic_posts_io(fakebook, arguments)

        else:
            print(MSG_UNKNOWN)
        
        command, arguments = next_command()

    print(BYE_MSG)
    
    
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
    # funÃ§Ã£o na main que trata da interacÃ§Ã£o com o utilizador para o
    # comando register
    # Assumindo que args == ['naive', 'Forrest', 'Gump']
    # entÃ£o args[0] = 'naive' e ' '.join(args[1:]) = 'Forrest Gump'

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


main()
