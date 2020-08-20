from django.test import TestCase, RequestFactory
from django.urls import resolve, reverse

from ..views import  (
    HomepageView, ProductsList, ProductDetail
)

from ..models import Categories, Products


class TestUrls(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.category = Categories.objects.create(
            name="Food"
        )

    def test_HomepageView_view_name(self):
        request = resolve("/shop/")
        self.assertEquals(request.view_name, "categories:homepage")

    def test_HomepageView_func_name(self):
        request = resolve("/shop/")
        self.assertTrue(request.func.__name__ == "HomepageView")

    def test_HomepageView_was_found(self):
        request = self.factory.get(reverse("categories:homepage"))
        response = HomepageView.as_view()(request)

        self.assertEquals(response.status_code, 200)

    def test_general_product_list_view_name(self):
        request = resolve("/shop/categories/general_product_list/")
        self.assertEquals(request.view_name, "categories:general_product_list")

    def test_general_product_list_page_was_found(self):
        request = self.factory.get("/shop/categories/general_product_list/")
        response = ProductsList.as_view()(request)

        self.assertEquals(response.status_code, 200)

    def test_categorised_product_list_view_name(self):
        request = resolve("/shop/categories/categorised_product_list/rice/")
        self.assertEquals(request.view_name, "categories:categorised_product_list")

    def test_categorised_product_list_func_name(self):
        request = resolve("/shop/categories/categorised_product_list/rice/")
        self.assertTrue(request.func.__name__ == "ProductsList")

    # def test_product_details_view_name(self):
    #     request = resolve("/shop/categories/product_details/")
