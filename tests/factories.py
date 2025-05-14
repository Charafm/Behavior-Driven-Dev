import factory
from factory.fuzzy import FuzzyChoice
from service.models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("word")
    category = FuzzyChoice(["Electronics", "Clothing", "Food"])
    available = FuzzyChoice([True, False])
    price = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)