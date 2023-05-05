from django.urls import path
from graphene_django.views import GraphQLView
from inventoryapp.schema import schema
from . import views

urlpatterns = [
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    # path("", views.item_list, name="item_list"),
    path("", views.item_home, name="item_home"),
    # path("", views.item_form, name="item_form"),
    # path("", views.item_bulk_upload, name="item_bulk_upload"),
]
