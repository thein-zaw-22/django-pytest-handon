import factory
from faker import Faker

from apps.blog.models import Post

fake = Faker()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyFunction(lambda: fake.sentence(nb_words=4))
    content = factory.LazyFunction(lambda: fake.paragraph(nb_sentences=3))
    is_published = True
