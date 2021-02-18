from abc_factory import AbstractFactory

factory = AbstractFactory.create_factory('Od')

parser = factory.create_parser()
analizer = factory.create_analizer()
sender = factory.create_sender()

parser.parse()
