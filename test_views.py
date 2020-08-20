from django.urls import resolve, reverse

from django.test import TestCase
from ..models import Categories, Products


class TestViews(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(
            name="Food"
        )

        self.category2 = Categories.objects.create(
            name="Books"
        )

        self.product = Products.objects.create(
            category_id=1,
            name="rice",
            price=345.56,
        )

        self.product2 = Products.objects.create(
            category_id=1,
            name="yam",
            price=345.56,
        )

        self.product3 = Products.objects.create(
            category_id=1,
            name="noodles",
            price=345.56,
        )

        self.product4 = Products.objects.create(
            category_id=2,
            name="Django",
            price=345.56,
        )
        self.products = Products.objects.all()


    def test_HomepageView_was_found(self):
        response = self.client.get(reverse("categories:homepage"))
        self.assertEquals(response.status_code, 200)

    def test_template_used_by_HomepageView(self):
        response = self.client.get("/shop/")
        self.assertTemplateUsed(response, "home.html")

    def test_general_product_list_page_was_found(self):
        response = self.client.get("/shop/categories/general_product_list/")
        self.assertEquals(response.status_code, 200)

    def test_categorised_product_list_page_was_found(self):
        response = self.client.get("/shop/categories/categorised_product_list/rice/")
        self.assertEquals(response.status_code, 200)

    def test_categorised_product_list_view_returns_products_under_the_specified_category(self):
        response = self.client.get(reverse("categories:categorised_product_list", args=["Food"]))
        self.assertGreaterEqual(len(response.context["products"]), 2)

    def test_general_product_list_view_returns_all_products_in_db_if_category_is_not_specified(self):
        response = self.client.get("/shop/categories/general_product_list/")
        self.assertGreater(len(response.context["products"]), 3)

    def test_template_used_by_general_product_list(self):
        response = self.client.get("/shop/categories/general_product_list/")
        self.assertTemplateUsed(response, "product_list.html")

    def test_template_used_by_categorised_product_list(self):
        response = self.client.get(reverse("categories:categorised_product_list", args=["Books"]))
        self.assertTemplateUsed(response, "product_list.html")

    def test_product_details_view_page_was_found(self):
        product_slug = self.products[1].slug
        response = self.client.get("/shop/categories/product_details/f'{product_slug}'/")
        self.assertEquals(response, "/shop/")


