class Article:

    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content):
        self.content = new_content

    def change_author(self, new_author):
        self.author = new_author

    def rename(self, new_title):
        self.title = new_title

    def __str__(self):
        return f"{self.title} - {self.content}: {self.author}"
