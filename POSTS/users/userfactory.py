from .user import User
from .userrepositories import UserRepositories
class UserFactory:

    def create_user(self, login: str, password: str):
        user = User(login=login, password=password)
        if UserRepositories.user_exist(UserRepositories, user):
            del user
            return print("User exist. Try another login.")
        else:
            UserRepositories.all_users.append(user)
            User.user_id_counter += 1
            print('User created')