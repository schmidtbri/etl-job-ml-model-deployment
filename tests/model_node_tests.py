import unittest
from traceback import print_tb

from model_etl.model_node import MLModelNode


# creating a mockup class to test with
class SomeClass(object):
    pass


class ModelManagerTests(unittest.TestCase):

    def test1(self):
        """ testing the MLModelNode class with good data """
        # arrange
        model_node = MLModelNode(module_name="iris_model.iris_predict", class_name="IrisModel")

        # act
        exception_raised = False
        # accessing the IrisModel model object
        try:
            generator = model_node(input={"sepal_length": 4.4, "sepal_width": 2.9, "petal_length": 1.4, "petal_width": 0.2})
            result = list(generator)
        except Exception as e:
            exception_raised = True
            print_tb(e)

        # assert
        self.assertFalse(exception_raised)
        self.assertTrue(result[0] is not None)

    def test2(self):
        """ testing the MLModelNode class with data with incorrect schema """
        # arrange
        model_node = MLModelNode(module_name="iris_model.iris_predict", class_name="IrisModel")

        # act
        exception_raised = False
        # accessing the IrisModel model object
        try:
            generator = model_node(input={"sepal_length": 4.4, "sepal_width": 2.9, "petal_width": 0.2})
            result = list(generator)
        except Exception as e:
            exception_raised = True
            print_tb(e)

        # assert
        print(result)
        self.assertFalse(exception_raised)
        self.assertTrue(result[0] is None)


if __name__ == '__main__':
    unittest.main()
