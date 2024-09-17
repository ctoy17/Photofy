from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Booking Date')),
                ('location', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('comment', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('V', 'Video'), ('P', 'Photo'), ('O', 'Other')], default='V', max_length=1, verbose_name='Equipment Type')),
                ('model', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('C', 'Card'), ('O', 'Online'), ('Z', 'Zelle'), ('X', 'Cash')], default='C', max_length=1, verbose_name='Payment Method')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Amount')),
                ('date', models.DateField(verbose_name='Transaction Date')),
                ('paid', models.BooleanField(verbose_name='Paid')),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('facebook', models.URLField(blank=True, max_length=250, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=250, null=True)),
                ('instagram', models.URLField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('equipments', models.ManyToManyField(blank=True, to='main_app.equipment')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=350)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
