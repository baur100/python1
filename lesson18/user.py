class User:
    active_user = 0
    def __init__(self, user_nickname, age):
        self.nick = user_nickname
        self.age = age
        User.active_user += 1

    @classmethod
    def display_number_or_users(cls):
        return cls.active_user

    @classmethod
    def ploshad_kruga(cls,radius):
        return 3.14*radius*radius




