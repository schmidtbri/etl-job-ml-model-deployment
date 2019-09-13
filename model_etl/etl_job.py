"""Module that runs bonobo graph on local files."""
import model_etl  # this import makes sure we can find site packages
from model_etl.graph import get_graph
import bonobo


def get_argument_parser(parser=None):
    """Extend CLI parser provided by bobobo and returns it."""
    parser = bonobo.get_argument_parser(parser=parser)

    parser.add_argument("--input_file", "-i", type=str, default=None, help="Path of the input file.")
    parser.add_argument("--output_file", "-o", type=str, default=None, help="Path of the output file.")

    return parser


if __name__ == '__main__':
    parser = get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services={}
        )
