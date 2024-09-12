import graphene
import graphql_jwt
from graphene import relay
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from apps.models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name']
        interfaces = relay.Node,


class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        category = Category.objects.create(name=name)
        return CreateCategory(category=category)


class Query(graphene.ObjectType):
    # category = relay.Node.Field(CategoryNode)
    # categories = DjangoConnectionField(CategoryNode)
    categories = graphene.List(CategoryType, page=graphene.Int(), page_size=graphene.Int(), order_by=graphene.String())
    category = graphene.Field(CategoryType, id=graphene.Int(required=True))

    @login_required
    def resolve_categories(self, info, page=1, page_size=3, name=None, order_by='id'):
        qs = Category.objects.order_by(order_by)
        if page and page_size:
            qs = qs[(page - 1) * page_size: page * page_size]
        return qs

    def resolve_category(self, info, id):
        return Category.objects.get(id=id)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
