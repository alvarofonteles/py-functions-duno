# %%
def func_nomeada():
    return 'Oi'


print(f'1 - {func_nomeada()}')
print(f'1.1 - {type(func_nomeada)}')  # <class 'function'>


def func_anomima(): return 'Oi'


print(f'2 - {func_anomima()}')
print(f'2.1 - {type(func_anomima)}')  # <class 'function'>

(lambda: 'Oi')()
print(f'3 - {(lambda: 'Oi')()}')


class FunctionClass:
    def __call__(self):
        return 'Oi'


print(f'4 - {FunctionClass()()}')

print(f'4.1 - {type(FunctionClass)}')  # <class 'type'>
print(f'4.2 - {type(FunctionClass())}')  # <class '__main__.FunctionClass'>
print(f'4.3 - {type(FunctionClass().__call__)}')  # <class 'method'>

minha_function_class = FunctionClass()

print(f'5 - {minha_function_class()}')
print(f'4.1 - {type(minha_function_class.__call__)}')  # <class 'method'>
