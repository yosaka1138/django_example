import re
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.core.validators import ValidationError


def number_only(value):
    if re.match(r"^[0-9]*$", value) is None:
        raise ValidationError(f"{value}s is not Number!")


class Friend(models.Model):
    name = models.CharField(max_length=100, validators=[RegexValidator(r"^[a-z]*$")])
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    # validation check
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    birthday = models.DateField()

    def __str__(self):
        return f"<Friend:id={str(self.id)},{self.name},({str(self.age)})>"
