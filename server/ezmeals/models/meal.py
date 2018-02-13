from django.db.models import Model
from django.db.models import fields


class Meal(Model):
    name = fields.CharField(max_length=255, null=False, blank=False)
    image = fields.CharField(max_length=255, null=False, blank=False)
