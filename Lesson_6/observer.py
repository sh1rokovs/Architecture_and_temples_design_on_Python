import abc
import time
import random


class Subject:
    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)


class Observer(metaclass=abc.ABCMeta):
    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class Sensor(Subject):
    @property
    def t(self):
        return self._subject_state

    @t.setter
    def t(self, t):
        self._subject_state = t
        self._notify()


class SmsNotifier(Observer):

    def update(self, arg):
        if arg > 50:
            print('send sms', 'куда так горячо!')


class DisplayObserver(Observer):
    def update(self, arg):
        print(f'{self.__class__.__name__} temperature {arg}')


class HeaterObserver(Observer):
    def __init__(self, low_threshold, step):
        super().__init__()
        self.low_threshold = low_threshold
        self.step = step

    def update(self, arg):
        if isinstance(self._subject, Sensor):
            sensor = self._subject

            t = sensor.t
            delta_low = t - self.low_threshold

            if delta_low < 0:
                t += self.step
                print(f'{self.__class__.__name__} heat impulse +{self.step}')
                sensor.t = t


# демо
sensor = Sensor()

# подключаем наблюдателей за сенсором
sensor.attach(DisplayObserver())
sensor.attach(HeaterObserver(40, 20))
sensor.attach(SmsNotifier())

# начальное значение
sensor.t = 20

# цикл энтропии – естественное охлаждение сенсора
for _ in range(5):
    random_t = random.random() * 10
    sensor.t = sensor.t - random_t
    time.sleep(0.5)
