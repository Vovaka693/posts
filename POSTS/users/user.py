class User:
    user_id_counter: int = 1

    def __init__(self, login: str, password: str):
        self.login: str = login
        self.password: str = password
        self.user_id: int = User.user_id_counter
        self.user_posts = []
        self.post_counter = 0


    def get_user_login(self):
        print(self.login)
        return self.login

    def get_user_password(self):
        print(self.password)
        return self.password

    def get_user_id(self):
        print(self.user_id)
        return self.user_id

    def get_user_posts(self):
        return self.user_posts