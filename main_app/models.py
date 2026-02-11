from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from datetime import date
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import MaxValueValidator, MinValueValidator




# Create your models here.
TYPES = (
    ('NORMAL', 'Normal'),
    ('DRY', 'Dry'),
    ('OILY', 'Oily'),
    ('COMBINATION', 'Combination'),
    ('SENSITIVE', 'Sensitive'),
)

CONCERN = (
    ('REDNESS', 'Redness'),
    ('DRYNESS', 'Dryness'),
    ('FINE LINES', 'Fine Lines'),
    ('ACNE', 'Acne'),
    ('SENSITIVITY', 'Sensitivity'),
    ('TEXTURE', 'Texture'),
    ('DARKSPOT', 'Darkspot'),
)

AVOIDED = (
    ('PARABENS', 'Parabens'),
    ('OILS', 'Oils'),
    ('FRAGRANCE', 'Fragrance'),
    ('SULFATES', 'Sulfates'),
    ('HARSH ALCOHOLS', 'Harsh Alcohols'),
    ('SILICONES', 'Silicones'),
)

ROUTINE_TIME = (
    ('MORNING AND EVENING','Morning and evening'),
    ('MORNING', 'Morning'),
    ('EVENING', 'Evening'),
    )

FREQUENCY=(
    ('EVERY DAY', 'Every Day'),
    ('EVERY OTHER DAY', 'Every other day'),
    ('EVERY 3 DAYS', 'Every 3 days'),
    ('EVERY 4 DAYS', 'Every 4 days'),
    ('EVERY WEEK', 'Every week'),
    ('ON SPECIFIC DAYS', 'On specific days'),
    ('AS NEEDED', 'As needed'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="main_app/static/uploads",blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    age = models.IntegerField(default=0)
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
        return f"{self.user.username}"



class TimeStamped(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Article(TimeStamped):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="main_app/static/uploads", default="")
    content= CKEditor5Field(config_name='extends')
    reading_time = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"



class Review(TimeStamped):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_description= models.TextField()
    image = models.ImageField(upload_to="main_app/static/uploads", blank=True, null=True)
    product_id = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.rating} {self.product_id}"


class Routine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s {self.name}"


class RoutineProduct(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=3)
    order = models.PositiveIntegerField(blank=False, default=100_000)
    time = models.CharField( max_length=50, choices=ROUTINE_TIME , default=ROUTINE_TIME[0][0])
    frequency = models.CharField( max_length=50, choices=FREQUENCY, default=FREQUENCY[0][0])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.product_id} {self.routine}"








