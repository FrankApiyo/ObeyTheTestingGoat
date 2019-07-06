from django import db

# Create your models here.
class Item(db.models.Model):
    text = db.models.TextField(default="")