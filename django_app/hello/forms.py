from cProfile import label
from random import choice
from django import forms


class HelloForm(forms.Form):
    id = forms.IntegerField(label="ID")


class HelloFormV2(forms.Form):
    data = [
        # requestのkey,表示される値
        ("one", "item 1"),
        ("two", "item 2"),
        ("three", "item 3"),
    ]
    choice = forms.ChoiceField(label="Choice", choices=data, widget=forms.RadioSelect())


class HelloFormV1(forms.Form):
    name = forms.CharField(
        label="name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    mail = forms.EmailField(
        label="mail", widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    age = forms.IntegerField(
        label="age",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        max_value=100,
        min_value=-100,
    )
