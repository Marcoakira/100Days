#Class
class User:  # name of class, have initial letter of world in upper. ( PascalCase)
    # constructor method
    def __init__(self, user_id, username):  # essa função que é chamada toda vez que for criado um objeto
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1
        user.username = "outro cara tem esse nome"
        self.username = " eu tenho esse nome"

# objects

user_0 = User('0022', 'incrivel')
user_1 = User('006', 'alguem')

user_0.follow(user_1)

print(user_0.followers)
print(user_0.following)
print(user_1.followers)
print(user_1.following)

print(user_0.username)
print(user_1.username)






# user_1 = User()
# user_1.id = '001'
# user_1.cocobongo = 'clube'
# user_1.sexo = 'robo'

# user_2 = User()
#
# print(user_1.cocobongo)
#
# print(user_2.cocobongo)


# class User:
#     def __init__(self, user_id, username):
#         self.id = len(user_id)
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
# user_1 = User("001", "nivia")
# user_2 = User("002", "marco")
#
# user_1.follow(user_2)
#
#
# print(user_1.followers)
# print(user_1.following)
#
#
# print(user_2.followers)
# print(user_2.following)
#

#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "angela"
#
#
#
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Marco"
#
# print(user_2.username)


# class Car:
#     def __init__(self):
#         self.seats = 5
#
#     def entre_race_mode(self):
#         self.seats = 2
#
#
#
#
# raposinha = Car()
#
# print(raposinha.entre_race_mode())
















