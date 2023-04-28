from django import forms
from .fields import GroupedModelChoiceField
from .models import Category, Item


class CategoryForm(forms.ModelForm):
    category = GroupedModelChoiceField(
        queryset=Category.objects.exclude(parent=None), choices_groupby="parent"
    )

    class Meta:
        model = Item
        fields = (
            "name_item",
            "description",
            "category",
            "quantity",
            "price",
            "created",
            "update",
        )
