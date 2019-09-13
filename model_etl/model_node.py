"""Code for running an MLModel class inside of a bonobo graph."""
import importlib

from ml_model_abc import MLModel, MLModelSchemaValidationException


class MLModelTransformer(object):
    """Transformation that loads and runs an MLModel class."""

    def __init__(self, module_name, class_name):
        """Instantiate MLModelTransformer class."""
        model_module = importlib.import_module(module_name)
        model_class = getattr(model_module, class_name)
        model_object = model_class()

        if isinstance(model_object, MLModel) is False:
            raise ValueError("The MLModelNode can only hold references to objects of type MLModel.")

        # saving the model reference
        self._model = model_object

    def __call__(self, data):
        """Receive data and send it to the MLModel object, returning prediction."""
        try:
            yield self._model.predict(data=data)
        except MLModelSchemaValidationException as e:
            raise e
