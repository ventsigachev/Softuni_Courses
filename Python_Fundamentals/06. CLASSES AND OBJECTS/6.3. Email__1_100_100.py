class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


e_mails = list()

while True:
    data = input()
    if data == "Stop":
        break
    [s, r, c] = data.split()
    email = Email(s, r, c)
    e_mails.append(email)

sent_emails = [int(x) for x in input().split(", ")]
for x in sent_emails:
    e_mails[x].sent()

for email in e_mails:
    print(email.get_info())
