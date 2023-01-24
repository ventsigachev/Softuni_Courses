class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


class EmailManager:
    def __init__(self):
        self.emails = []

    def add(self, email):
        self.emails.append(email)

    def sent(self, index):
        self.emails[index].send()

    def print(self):
        for email in self.emails:
            print(email.get_info())


emailManager = EmailManager()

while True:
    info = input()
    if info == 'Stop':
        break
    [s, r, c] = info.split(' ')

    emailManager.add(Email(s, r, c))

indices_of_mails_to_send = map(int, input().split(', '))

for i in indices_of_mails_to_send:
    emailManager.sent(i)

emailManager.print()
