# Generated by Django 3.2.7 on 2021-11-16 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0018_shopping_card_shipping_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_card',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shoppingCardOfUser', to=settings.AUTH_USER_MODEL, verbose_name="Which User's shopping card?"),
        ),
    ]
