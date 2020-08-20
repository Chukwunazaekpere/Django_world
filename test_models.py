from django.test import TestCase

from ..models import Categories, Products


class TestModels(TestCase):
    def setUp(self):
        self.category = Categories()
        self.product = Products()

        self.food_category = Categories.objects.create(
            name="Food",
        )
        self.all_categories = Categories.objects.all()

        self.rice_product = Products.objects.create(
            category_id=1,
            name="rice",
            price="300.45",
        )
        self.all_products = Products.objects.all()

    def test_categories_model_attributes(self):
        category_name_title = self.category._meta.get_field("name").verbose_name
        self.assertTrue(category_name_title == "name")

    def test_categories_save_method(self):
        self.assertGreaterEqual(Categories.objects.count(), 1)  # objects of Categories model gets saved.
        self.assertIsNotNone(self.all_categories[0].slug)  # slug field of objects are prepopulated upon save.

    # def test_categories_get_absolute_url(self):
    #     self.assertEquals(self.all_categories[0].get_absolute_url(), "/shop/categories/food/")

    def test_products_model_attributes(self):
        product_name_field_title = self.rice_product._meta.get_field('name').verbose_name
        self.assertTrue(product_name_field_title == 'name')

    def test_product_model_save_method(self):
        self.assertGreaterEqual(Products.objects.count(), 1)

    def test_product_model_get_absolute_url_method(self):
        product = Products.objects.all()
        self.assertEquals(product[0].get_absolute_url(),
                          f"/shop/categories/product_details/{product[0].slug}/")


