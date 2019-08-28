import bonobo
from bonobo.nodes.io.json import LdjsonReader, LdjsonWriter
from model_etl.model_node import MLModelTransformer


def get_graph(input_file, output_file):
    graph = bonobo.Graph()
    graph.add_chain(LdjsonReader(input_file),
                    MLModelTransformer(module_name="iris_model.iris_predict", class_name="IrisModel"),
                    LdjsonWriter(output_file))
    return graph


def get_services(**options):
    return {}


def get_argument_parser(parser=None):
    parser = bonobo.get_argument_parser(parser=parser)

    parser.add_argument("--input_file", "-i", type=str, default=None, help="Path of the input file.")
    parser.add_argument("--output_file", "-o", type=str, default=None, help="Path of the output file.")

    return parser


if __name__ == '__main__':
    parser = get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=get_services(**options)
        )
