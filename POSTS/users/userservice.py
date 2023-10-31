from user import User  as U
from userfactory import UserFactory as UF
from userrepositories import UserRepositories as UR
# from posts import Posts as P

class UserService:

    def new_user(self, login, password):
        return UF.create_user(UF, login=login, password=password)



us = UserService()
user1 = us.new_user('vovaka', 'password')
user1.get_user_login()
print(UR.all_users)