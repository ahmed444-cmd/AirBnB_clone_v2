#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity


class TestAmenity(TestBasemodel):
    """Represents the aminity test models."""
    def __init__(self, *args, **kwargs):
        """Begins test class."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Tests the typed name."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
