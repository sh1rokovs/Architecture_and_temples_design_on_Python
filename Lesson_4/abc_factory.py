import abc


class Parser(abc.ABC):

    @abc.abstractmethod
    def parse(self):
        pass


class VkParser(Parser):

    def parse(self):
        print('Vk parser work')


class VkAnalizer:
    pass


class VkSender:
    pass


class OdParser(Parser):

    def parse(self):
        print('Od parser work')


class OdAnalizer:
    pass


class OdSender:
    pass


class AbstractFactory(abc.ABC):

    @staticmethod
    def create_factory(network_name):
        NETWORKS = {
            'Vk': VkFactory,
            'Od': OdFactory
        }

        return NETWORKS[network_name]()

    @abc.abstractmethod
    def create_parser(self):
        pass

    @abc.abstractmethod
    def create_analizer(self):
        pass

    @abc.abstractmethod
    def create_sender(self):
        pass


class VkFactory(AbstractFactory):

    def create_parser(self):
        return VkParser()

    def create_analizer(self):
        return VkAnalizer()

    def create_sender(self):
        return VkSender()


class OdFactory(AbstractFactory):

    def create_parser(self):
        return OdParser()

    def create_analizer(self):
        return OdAnalizer()

    def create_sender(self):
        return OdSender()
