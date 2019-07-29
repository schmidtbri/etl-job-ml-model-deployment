import bonobo


def extract():
    yield 'hello'
    yield 'world'


def transform(*args):
    yield tuple(
        map(str.title, args)
    )


def load(*args):
    print(*args)


def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(extract, transform, load)

    return graph


def get_services(**options):
    return {}


if __name__ == '__main__':
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=get_services(**options)
        )
