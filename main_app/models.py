from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
TYPES = (
    ('N', 'Normal'),
    ('D', 'Dry'),
    ('O', 'Oily'),
    ('C', 'Combination'),
    ('S', 'Sensitive'),
)

CONCERN = (
    ('R', 'Redness'),
    ('D', 'Dryness'),
    ('F', 'Fine Lines'),
    ('A', 'Acne'),
    ('S', 'Sensitivity'),
    ('T', 'Texture'),
    ('H', 'Darkspot'),
)

AVOIDED = (
    ('P', 'Parabens'),
    ('O', 'Oils'),
    ('F', 'Fragrance'),
    ('S', 'Sulfates'),
    ('A', 'Harsh Alcohols'),
    ('D', 'Silicones'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="main_app/static/uploads", default="")
    bio = models.TextField()
    age = models.IntegerField()
    skin_type = models.CharField(max_length=15, choices=TYPES, default=TYPES[0][0])
    skin_concern = ArrayField(
        models.CharField(max_length=20, choices=CONCERN),
        blank=False,
        default=list,
        )
    avoided_ingredients =  ArrayField(
        models.CharField(max_length=30, choices=AVOIDED),
        blank=True,
        default=list,
        )

    def __str__(self):
        return self.user.username
