from django.test import TestCase
from inventoryapp.models import Category, Item
from datetime import datetime


class CategoryTestCase(TestCase):
    def setUp(self):
        # create some test data
        Category.objects.create(category_name="Books")

    def test_category_model(self):
        # retrieve the test data
        my_model = Category.objects.get(category_name="Books")

        # check that the data was created correctly
        self.assertEqual(my_model.category_name, "Books")


class ItemTestCase(TestCase):
    def setUp(self):
        # create some test data
        category = Category.objects.create(category_name="Books")

        Item.objects.create(
            name_item="science",
            description="science books",
            category=category,
            quantity=12,
            price=123,
        )

    def test_item_model(self):
        # retrieve the test data
        category = Category.objects.get(category_name="Books")

        my_model = Item.objects.get(
            name_item="science",
            description="science books",
            quantity=12,
            price=123,
            category=category,
        )

        # check that the data was created correctly
        self.assertEqual(my_model.name_item, "science")
        self.assertEqual(my_model.description, "science books")
        self.assertEqual(my_model.category.category_name, "Books")
        self.assertEqual(my_model.quantity, 12)
        self.assertEqual(my_model.price, 123)
