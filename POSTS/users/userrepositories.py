class UserRepositories:
    all_users = []

    def user_exist(self, user):
        for i in UserRepositories.all_users:
            if user.login == i.login:
                return True
            else:
                return False

    def get_all_users(self):
        for user in UserRepositories.all_users:
            print(user.user_id, ". ",user.login)

    def insert_user(self, user):
        if not UserRepositories.user_exist(user):
            UserRepositories.all_users.append(user)
            print(f"User {user.login} added to the database with ID: {user.user_id}")
        else:
            return print("User exist")

    def change_password(self, user, old_password, new_password):
        if old_password == user.password:
            user.password = new_password
            # self.update_user_in_database(user)

    def change_login(self, user, new_login, password):
        if password == user.password:
            old_login = user.login
            user.login = new_login
            return "Login changed successfully"
        else:
            return "Password is incorrect. Login not changed."


    def delete_user(self, login, password):
        counter = 0
        for user in UserRepositories.all_users:
            if login == user.login and login.password == password:
                del UserRepositories.all_users[counter]
                return print(f"User {login.login} has been deleted from the database.")
                counter += 1
        return print("User not found in the database.")

    def find_user(self, login=None, user_id=None):
        for user in UserRepositories.all_users:
            if user.login == login or user.user_id == user_id:
                return user
        return "User not found!"