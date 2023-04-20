import graphene
from graphene_django import DjangoObjectType

from .models import Item


class ItemType(DjangoObjectType):
    class Meta:
        model = Item
        fields = ("id", "name_item", "description")


class Query(graphene.ObjectType):
    all_items = graphene.List(ItemType)

    def resolve_all_items(root, info):
        # We can easily optimize query count in the resolve method
        return Item.objects.all()


schema = graphene.Schema(query=Query)
