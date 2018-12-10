import datetime

class Member():
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age
        self.id = 0
        self.posts = []

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Post():
    def __init__(self, title = None, content = None, member_id = None):
        self.title = title
        self.content = content
        self.id = 0
        self.member_id = member_id
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}, Date: {self.date}"
