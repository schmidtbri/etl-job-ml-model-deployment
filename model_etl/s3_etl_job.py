"""Module that runs bonobo graph on files in S3 service."""
import model_etl  # this import makes sure we can find site packages
from model_etl.graph import get_graph
import bonobo
from fs_s3fs import S3FS


def get_services(**options):
    """Instantiate an S3 filesystem service for loading and saving files from the ETL."""
    return {
        'fs': S3FS(options["bucket"],
                   aws_access_key_id=options["key"],
                   aws_secret_access_key=options["secret_key"],
                   endpoint_url=options["endpoint_url"],)
    }


def get_argument_parser(parser=None):
    """Extend CLI parser provided by bobobo and returns it."""
    parser = bonobo.get_argument_parser(parser=parser)

    parser.add_argument("--input_file", "-i", type=str, default=None, help="Path of the input file.")
    parser.add_argument("--output_file", "-o", type=str, default=None, help="Path of the output file.")

    # these parameters are added for accessing different S3 services
    parser.add_argument("--bucket", "-b", type=str, default=None, help="Bucket name in S3 service.")
    parser.add_argument("--key", "-k", type=str, default=None, help="Key to access S3 service.")
    parser.add_argument("--secret_key", "-sk", type=str, default=None, help="Secret key to access the S3 service.")
    parser.add_argument("--endpoint_url", "-ep", type=str, default=None, help="Endpoint URL for S3 service.")

    return parser


if __name__ == '__main__':
    parser = get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=get_services(**options)
        )
