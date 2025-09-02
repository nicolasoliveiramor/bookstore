import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.product = ProductFactory(
            title="pro controller",
            price=200.00,
        )

    def test_get_all_product(self):
        response = self.client.get(reverse("product-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)

        self.assertEqual(product_data["results"][0]["title"], self.product.title)
        self.assertEqual(product_data["results"][0]["price"], self.product.price)
        self.assertEqual(product_data["results"][0]["active"], self.product.active)

    def test_create_product(self):
        category = CategoryFactory()
        data = json.dumps(
            {"title": "notebook", "price": 800.00, "categories_id": [category.id]}
        )

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title="notebook")

        self.assertEqual(created_product.title, "notebook")
        self.assertEqual(created_product.price, 800.00)

    def test_delete_Product(self):
        product = ProductFactory(price=150)

        response = self.client.delete(
            reverse("product-detail", kwargs={"version": "v1", "pk": product.id})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(price=150).exists())
