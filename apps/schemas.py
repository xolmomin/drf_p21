import graphene
from graphene_django import DjangoObjectType

from apps.models import Product, Category


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, name):
        """
        The mutate function is the function that will be called when a client
        makes a request to this mutation. It takes in four arguments:
        self, info, title and content. The first two are required by all mutations;
        the last two are the arguments we defined in our CreatePostInput class.

        :param self: Access the object's attributes and methods
        :param info: Access the context of the request
        :param title: Create a new post with the title provided
        :param content: Pass the content of the post
        :param author_id: Get the author object from the database
        :return: A createpost object
        """
        category = Category.objects.create(
            name=name
        )
        return CreateCategory(category=category)


class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    categories = graphene.List(CategoryType, description='Bu kategoriya hisoblanadi')

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_categories(self, info):
        return Category.objects.all()


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
