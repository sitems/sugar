from werkzeug.routing import Map, Rule


class Sugar:
    """
    Usually you create a :class:`Sugar` instance in your main module or
    in the `__init__.py` file of your package like this::

    from sugar import Sugar
    app = Flask()
    """
    secret_key = '9b7+8l35&)ldkw%5w)bg_0f=2^+%o9floh8_v)-4k0n)4^98jl'

    def __init__(self):
        self.urlmappings = dict()
        self.error_handlers = dict()
        self.url_map = Map()