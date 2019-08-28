import unittest
from traceback import print_tb

from model_etl.model_node import MLModelTransformer


# creating a mockup class to test with
class SomeClass(object):
    pass


class ModelManagerTests(unittest.TestCase):

    def test1(self):
        """ testing the MLModelNode class with good data """
        # arrange
        model_node = MLModelTransformer(module_name="iris_model.iris_predict", class_name="IrisModel")

        # act
        exception_raised = False
        # accessing the IrisModel model object
        try:
            generator = model_node(data={"sepal_length": 4.4, "sepal_width": 2.9, "petal_length": 1.4, "petal_width": 0.2})
            result = list(generator)
        except Exception as e:
            exception_raised = True

        # assert
        self.assertFalse(exception_raised)

    def test2(self):
        """ testing the MLModelNode class with data with incorrect schema """
        # arrange
        model_node = MLModelTransformer(module_name="iris_model.iris_predict", class_name="IrisModel")

        # act
        exception_raised = False
        result = []
        # accessing the IrisModel model object
        try:
            generator = model_node(data={"sepal_length": 4.4, "sepal_width": 2.9, "petal_width": 0.2})
            result = list(generator)
        except Exception as e:
            exception_raised = True

        # assert
        self.assertTrue(exception_raised)


if __name__ == '__main__':
    unittest.main()
