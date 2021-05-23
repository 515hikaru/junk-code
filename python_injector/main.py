from injector import Injector, InstanceProvider, inject


class A:
    @inject
    def __init__(self, number: int, name: str):
        self.number = number
        self.name = name

class B:
    @inject
    def __init__(self, a: A):
        self.a = a

    @inject
    def b(self, keyword: str):
        print(keyword, [self.a.name, self.a.number])

def configure(binder):
    binder.bind(A, to=InstanceProvider(A(10, 'hikaru')))
    # binder.bind(int, 10)
    # binder.bind(str, 'hikaru')


def main():
    injector = Injector()
    b = injector.get(B)
    print(b.a.number)
    print(b.a.name)

    configured_injector = Injector(configure)
    configured_injector.call_with_injection(configured_injector.get(B).b)
    configured_injector.call_with_injection(configured_injector.get(B).b, args=('foo',))


if __name__ == '__main__':
    main()
