from traceback import format_stack


class InstantiationError(Exception):
    pass


def make(fn):
    added = False

    def _make(cls, *args, **kwargs):
        nonlocal added

        if not added:
            methods: set[str] = getattr(cls, "__factory_methods")
            methods.add(fn.__name__)
            added = True

        return fn(cls, *args, **kwargs)

    return _make


def factory(cls):
    methods: set[str] | None = getattr(cls, "__factory_methods", None)
    if methods is None:
        methods = set()
        setattr(cls, "__factory_methods", methods)

    old_init = getattr(cls, "__init__")

    def patch_init(self, *args, **kwargs):
        i = -1
        allowed = False

        for trace in reversed(format_stack()):
            i += 1

            if i == 0:
                continue

            if i > 3:
                break

            callee = trace.split("\n")[0].split(" ")[-1]
            if callee in methods:
                allowed = True
                break

        if not allowed:
            raise InstantiationError(f"Not allowed to instantiate {type(self).__name__} directly")

        old_init(self, *args, **kwargs)

    setattr(cls, "__init__", patch_init)

    return cls
