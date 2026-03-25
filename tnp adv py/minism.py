class User:
    def __init__(self, name):
        self.name = name

class Post:
    total = 0
    def __init__(self, content):
        self.content = content
        Post.total += 1
        self.comments = []

    def add_comment(self, c):
        self.comments.append(c)

    def __str__(self):
        return self.content

class Comment:
    def __init__(self, text):
        self.text = text