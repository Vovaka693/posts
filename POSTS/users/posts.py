class Posts:

    amountOfPosts: int = 0
    all_posts = []

    def __init__(self, user, text: str):
        user.post_counter += 1
        self.post_id = Posts.amountOfPosts
        self.post_text = text
        self.add_post_to_colection(user)

    def add_post_to_colection(self, user):
        user.user_posts.append({'postID': self.post_id, 'postText': self.post_text})
        Posts.all_posts.append({'postID': self.post_id, 'postText': self.post_text, 'user_id': user.user_id})
        Posts.amountOfPosts += 1

    def delete_post(self, postID):
        post = self.find_post(postID)
        if post:
            del post
            return "Post deleted!"
        else:
            return "Delete error!!"

    def find_post(self, postID):
        for post in Posts.all_posts:
            if post['postID'] == postID:
                return post
        print("Post not found!!")
        return None

    def change_post(self, postID):
        post = self.find_post(postID)
        if post:
            changed_text = input(f'What you want to change: {post["postText"]}... ')
            post['postText'] = changed_text
            return f'Post {post["postID"]} was changed!'
        else:
            return 'Change error!!'