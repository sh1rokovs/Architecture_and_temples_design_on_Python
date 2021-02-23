import abc


class Notifier(metaclass=abc.ABCMeta):
    def __init__(self):
        self._log_list = []

    def notify(self, address, subject, message):
        self._login()
        self._send(address, subject, message)
        self._logout()
        self._log(address, subject, message)

    # войти в ситему доставки сообщений
    @abc.abstractmethod
    def _login(self):
        pass

    # отправка сообщения
    @abc.abstractmethod
    def _send(self, address, subject, message):
        pass

    # выход
    @abc.abstractmethod
    def _logout(self):
        pass

    # внутреннее логирование, задаем поведение по умолчанию
    def _log(self, address, subject, message):
        self._log_list.append([address, subject, message])


class EmailNotifier(Notifier):
    def __init__(self):
        super().__init__()
        self.mail_from = ''

    def _login(self):
        # no need to login
        pass

    def _send(self, mail_to, subject, message):
        # send_mail(self.mail_from, mail_to, subject, message)
        print(f'send_mail: {mail_to}, {subject}, {message}')

    def _logout(self):
        # no need to logout
        pass


class FacebookNotifier(Notifier):
    def _login(self):
        # login to facebook
        print('login to facebook')

    def _send(self, address, subject, message):
        # send facebook message
        print(f'send facebook message: {address}, {subject}, {message}')

    def _logout(self):
        # logout from facebook
        print('logout from facebook')

    # переопределяем поведение шага внутреннего логирования
    def _log(self, address, subject, message):
        # не будем внутренне логировать нотификацию по FB, ибо это избыточно.
        pass


class NotifierFabric:
    @staticmethod
    def get_notifier(communication_type):
        if communication_type == 'EMAIL':
            return EmailNotifier()
        elif communication_type == 'FACEBOOK':
            return FacebookNotifier()
        # ...


# инстанциируем объект конкретного нотификатора, используя паттерн Фабричный метод
notifier_1 = NotifierFabric.get_notifier('EMAIL')
notifier_1.notify('patterns@geekbrains.ru', 'notify_1', 'hello world')
print(notifier_1.__dict__)

# инстанциируем объект конкретного нотификатора
notifier_2 = NotifierFabric.get_notifier('FACEBOOK')
notifier_2.notify('patterns_facebook', 'notify_2', 'hi')
print(notifier_2.__dict__)


# from django.views.generic import ListView
#
#
# class MyListView(ListView):
#
#     def get_queryset(self):
#         return ...
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         pass


