import bonobo
from bonobo.nodes.io.json import LdjsonReader, LdjsonWriter
from model_etl.model_node import MLModelNode


def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(LdjsonReader('data/input.json'),
                    MLModelNode(module_name="iris_model.iris_predict", class_name="IrisModel"),
                    LdjsonWriter("data/output.json"))
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
