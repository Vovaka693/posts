from users.user import User
from users.userrepositories import UserRepositories
from users.userfactory import UserFactory
from users.posts import Posts

ur = UserRepositories()
uf = UserFactory()
uf.create_user('vovaka', 'password')
ur.get_all_users()
post = Posts(user=ur.find_user('vovaka'), text="First post!")
print(post.all_posts)
print(post.find_post(0))
uf.create_user('vovaka1', 'passwordd')
ur.get_all_users()
user = ur.find_user(user_id=1)
ur.change_login(user=user, new_login='vovaka420', password='passwordd')
ur.get_all_users()
user = ur.find_user(user_id=1)
ur.change_password(user=user, old_password='passwordd', new_password='password420')
ur.get_all_users()
ur.find_user(login='vovaka')
result = ur.change_login(user=user, new_login='vovaka420', password='password')
print(result)
ur.get_all_users()