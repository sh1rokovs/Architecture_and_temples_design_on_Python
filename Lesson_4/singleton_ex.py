class Origin:
    pass


o1 = Origin()
o2 = Origin()  # 1. запрещено, 2. возвращает ссылку на уже созданный экземпляр

print(o2 is o1)

a = []

b = a

print(a is b)

b = a.copy()

print(a is b)

a = []
b = []

print(a is b)

# Вселенная (Параллельные вселенные)

# Логгер, Настройки программы