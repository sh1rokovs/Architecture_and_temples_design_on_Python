class MimeMessage:
    def __init__(self, session):
        self.session = session


# построитель сообщения электронной почты
class MimeMessageBuilder:
    def __init__(self, session):
        self.message = MimeMessage(session)

    # def add_some(self, some):
    #     self.message.some = some

    # def add_some(self, some):
    #     self.message.some = some
    #     return self.message

    def from_addr(self, address):
        self.message._from_addr = address
        return self

    def to_addr(self, address):
        self.message._to_addr = address
        return self

    def cc_addr(self, address):
        self.message._cc_addr = address
        return self

    def subject(self, subject):
        self.message._subject = subject
        return self

    def body(self, body):
        self.message._body = body
        return self

    def build(self):
        return self.message


class Client:
    def send_mail(session):
        message = MimeMessageBuilder(session). \
            from_addr('me').to_addr('you').cc_addr('someone'). \
            subject('test').body('hello'). \
            build()

# 1 ничего не возвращаем
# builder = MimeMessageBuilder(session)
# builder.add_some()
# builder.add_some2()
# builder.add_some3()
# builder.message
# # 2 возвращаем message
# builder = MimeMessageBuilder(session)
# message = builder.add_some()
# message = builder.add_some2()
# message = builder.add_some3()
# return self


