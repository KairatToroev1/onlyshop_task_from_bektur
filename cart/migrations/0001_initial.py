# Generated by Django 3.2.7 on 2021-10-07 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('magazin', '0003_alter_production_raiting'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartproduct', to='cart.cart')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartproduction', to='magazin.production')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(related_name='carts', through='cart.CartProduct', to='magazin.Production'),
        ),
    ]
