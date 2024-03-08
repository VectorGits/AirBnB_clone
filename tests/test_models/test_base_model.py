#!/usr/bin/python3
"""BaseModel Tests"""

from models.base_model import BaseModel
import unittest
import pycodestyle
import inspect
import uuid
from datetime import datetime


class TestDocumentation(unittest.TestCase):
    """Test documentation for models/base.py"""

    # test 1
    def test_class_docstring(self):
        """Method to test if class has a docstring."""

        self.assertIsNotNone(BaseModel.__doc__)

    # test 2
    def test_method_docstring(self):
        """Method to test if class method has a docstring."""

        self.assertIsNotNone(BaseModel.__init__.__doc__)


class TestPycodestyle(unittest.TestCase):
    """Test Pycodestyle compliance for models/base.py"""

    # test 3
    def test_pycodestyle(self):

        checker = pycodestyle.StyleGuide().check_files(["models/base_model.py"])

        self.assertEqual(checker.total_errors, 0)


class TestBaseModelClass(unittest.TestCase):
    """Test cases for the BaseModel class."""

    # prep
    def setUp(self):
        """Create an instance of BaseModel before each test method."""

        self.bm1 = BaseModel()

    # test 4
    def test_base_model_class_methods(self):
        """Test the BaseModel class methods."""

        self.assertTrue(inspect.isfunction(getattr(BaseModel, "__init__")))
        self.assertTrue(inspect.isfunction(getattr(BaseModel, "__str__")))
        self.assertTrue(inspect.isfunction(getattr(BaseModel, "save")))
        self.assertTrue(inspect.isfunction(getattr(BaseModel, "to_dict")))

    # test 5
    def test_base_model_constructor_method(self):
        """Test the BaseModel class constructor attribute."""

        self.assertIn("args", inspect.signature(BaseModel.__init__).parameters)
        self.assertIn("kwargs", inspect.signature(BaseModel.__init__).parameters)
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertTrue(hasattr(self.bm1, "created_at"))
        self.assertTrue(hasattr(self.bm1, "updated_at"))

    # test 6
    def test_base_model_constructor_method_with_kwargs(self):
        """Test the BaseModel class constructor if kwargs is not empty."""

        class_attr = [attr for attr in dir(BaseModel) if not attr.startswith("__")]
        test_kwargs = {attr: f"value_{attr}" for attr in class_attr}
        bm2 = BaseModel(**test_kwargs)
        for key, value in test_kwargs.items():
            if key != "__class__":
                self.assertTrue(hasattr(bm2, key))
                self.assertTrue(getattr(bm2, key), value)

    # test 7
    def test_base_model_id_attribute(self):
        """Test the id instance."""

        self.assertIsInstance(self.bm1.id, str)
        self.assertTrue(uuid.UUID(self.bm1.id))
        bm2 = BaseModel()
        self.assertNotEqual(self.bm1.id, bm2.id)

    # test 8
    def test_base_model_created_at_attribute(self):
        """Test the created_at instance."""

        self.assertIsInstance(self.bm1.created_at, datetime)

    # test 9
    def test_base_model_updated_at_attribute(self):
        """Test the updated_at instance."""

        self.assertIsInstance(self.bm1.updated_at, datetime)

    # test 10
    def test_base_model_str_method(self):
        """Test the string representation of BaseModel."""

        test_string = str(self.bm1)

        self.assertIsInstance(test_string, str)
        self.assertIn(type(self.bm1).__name__, test_string)
        self.assertIn(f"({self.bm1.id})", test_string)
        self.assertIn(str(self.bm1.__dict__), test_string)

    # test 11
    def test_base_model_save_method(self):
        """Test the save method of BaseModel."""

        initial_datetime = self.bm1.updated_at

        self.bm1.save()
        self.assertNotEqual(initial_datetime, self.bm1.updated_at)

    # test 12
    def test_base_model_to_dict_method(self):
        """Test the to_dict method of BaseModel."""

        test_dict = self.bm1.to_dict()

        self.assertIsInstance(test_dict, dict)
        self.assertIn("__class__", test_dict)
        self.assertEqual(test_dict["__class__"], "BaseModel")
        self.assertIn("created_at", test_dict)
        self.assertIn("updated_at", test_dict)
        cac = datetime.fromisoformat(test_dict["created_at"])
        uac = datetime.fromisoformat(test_dict["updated_at"])
        self.assertIsInstance(cac, datetime)
        self.assertIsInstance(uac, datetime)
        self.assertEqual(cac, self.bm1.created_at)
        self.assertEqual(uac, self.bm1.updated_at)
        self.assertIn("id", test_dict)
        self.assertEqual(test_dict["id"], self.bm1.id)
