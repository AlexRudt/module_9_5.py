class StepValueError(ValueError):
    pass
class Iterator():
    def __init__(self, start, stop, step = 1):
        self.start = start  # start - целое число, с которого начинается итерация.
        self.stop = stop    # stop - целое число, на котором заканчивается итерация.
        self.step = step    # step - шаг, с которым совершается итерация (по умолчанию =1).
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start   # pointer - указывает на текущее число в итерации (изначально start)
        return self # возвращаем ссылку на самого себя, т.к. наш объект должен быть итератором

    def __next__(self):
        self.pointer += self.step   # увеличиваем атрибут pointer на step
        if self.step < 0:
            if self.pointer < self.stop:
                raise  StopIteration()
        else:
            if self.pointer > self.stop:
                raise  StopIteration()
        return self.pointer

try:
    iter1 = Iterator(100, 200, 0)
    for k in iter1:
        print(k, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

