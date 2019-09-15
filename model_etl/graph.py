"""Module that builds the ETL DAG."""
import bonobo
from bonobo.nodes.io.json import LdjsonReader, LdjsonWriter

from model_etl.model_node import MLModelTransformer


def get_graph(**options):
    """Define a graph that loads data ldjson file, transforms it with the IrisModel class, and saves the results to an ldjson file."""
    graph = bonobo.Graph()
    graph.add_chain(LdjsonReader(options["input_file"], mode='r'),
                    MLModelTransformer(module_name="iris_model.iris_predict", class_name="IrisModel"),
                    LdjsonWriter(options["output_file"], mode='w'))
    return graph
