class CommandsInvoker:
    def __init__(self):
        self._commands_list = []

    def store_command(self, command):
        self._commands_list.append(command)

    def execute_commands(self):
        for command in self._commands_list:
            print('execute', dir(command))
            command()


def action():
    print('action in receiver')


def pause():
    print('pause in receiver')


def param_command(param):
    print(f'console {param}')


def param_close():
    param_command('my param')


class ParamClass:

    def __init__(self, param):
        self.param = param

    def __call__(self, *args, **kwargs):
        print(f'console {self.param}')


command_invoker = CommandsInvoker()

command_invoker.store_command(action)
command_invoker.store_command(pause)
command_invoker.store_command(param_close)
command_invoker.store_command(ParamClass('my param'))
command_invoker.store_command(lambda: param_command('my param'))

command_invoker.execute_commands()