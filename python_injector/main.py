from typing import Dict

from injector import Injector, inject

from .cache import DictCache, ICache


def cache_config(binder):
    binder.bind(ICache, DictCache)


class FooCase:

    @inject
    def __init__(self, cache: ICache):
        self.cache = cache

    def execute(self):
        v = self.cache.get('foo')
        if v is None:
            v = 'no cache'
        print(v)


def main():
    injector = Injector(cache_config)
    foo = injector.get(FooCase)
    foo.execute()


if __name__ == '__main__':
    main()
