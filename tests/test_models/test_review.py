#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import TestBasemodel
from models.review import Review


class TestReview(TestBasemodel):
    """Represents tests for Review model."""
    def __init__(self, *args, **kwargs):
        """Initializes test class."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Tests type of place_id."""
        new = self.value()
        self.assertEqual(
            type(new.place_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_user_id(self):
        """Tests type of user_id."""
        new = self.value()
        self.assertEqual(
            type(new.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_text(self):
        """Tests type of text."""
        new = self.value()
        self.assertEqual(
            type(new.text),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
