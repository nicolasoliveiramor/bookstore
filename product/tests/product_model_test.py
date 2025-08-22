import pytest

from product.models import Product

@pytest.mark.django_db # Permite o pytest acessar o banco de dados do Django
def test_create_product():
    product = Product.objects.create(
        title="Produto 1",
        description="Produto de teste.",
        price=100
    )
    assert product.title == "Produto 1"
    assert product.description == "Produto de teste."
    assert product.price == 100
    assert product.id is not None