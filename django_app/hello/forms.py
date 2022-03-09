from django import forms

from hello.models import Friend, Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["title", "content", "friend"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control form-control-sm",
                    "rows": 2,
                }
            ),
            "friend": forms.Select(attrs={"class": "form-control form-control-sm"}),
        }


class CheckForm(forms.Form):
    string = forms.CharField(
        label="String",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        string = cleaned_data["string"]
        if string.lower().startswith("no"):
            raise forms.ValidationError("You input 'NO'!")


class CheckFormV1(forms.Form):
    string = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )


class FindForm(forms.Form):
    find = forms.CharField(
        label="Find",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ["name", "mail", "gender", "age", "birthday"]


class HelloForm(forms.Form):
    name = forms.CharField(
        label="Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    mail = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    gender = forms.BooleanField(
        label="Gender",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check"}),
    )
    age = forms.IntegerField(
        label="Age", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    birthday = forms.DateField(
        label="Birth", widget=forms.DateInput(attrs={"class": "form-control"})
    )


class HelloFormV3(forms.Form):
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
