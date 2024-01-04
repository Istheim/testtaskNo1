from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from user.models import User

NULLABLE = {'blank': True, 'null': True}


class NetworkElement(models.Model):
    FACTORY = '0'
    RETAIL = '1'
    IP = '2'
    LEVELS_CHOICES = [
        (FACTORY, 'Factory'),
        (RETAIL, 'Retail'),
        (IP, 'IP'),
    ]

    name = models.CharField(max_length=64, verbose_name='Название')
    level = models.CharField(max_length=7, choices=LEVELS_CHOICES, default=IP, verbose_name='Уровень')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE)

    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name='Задолженность')
    creation_time = models.DateTimeField(default=timezone.now, verbose_name='Время создания')

    email = models.EmailField(max_length=64, verbose_name='Почта', unique=True)
    country = models.CharField(max_length=64, verbose_name='Страна')
    city = models.CharField(max_length=64, verbose_name='Город')
    street = models.CharField(max_length=64, verbose_name='Улица')
    number_house = models.IntegerField(verbose_name='Номер дома')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    products = models.CharField(max_length=64, verbose_name='Продукт')
    model = models.CharField(max_length=64, verbose_name='Модель')
    date = models.DateField(verbose_name='Дата выхода на рынок', **NULLABLE)

    def clean(self):
        supplier_levels = dict(NetworkElement.LEVELS_CHOICES)
        if supplier_levels[self.supplier] >= supplier_levels[self.level]:
            raise ValidationError("Supplier must be at a lower level in the hierarchy.")
        super().clean()

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"

    class Meta:
        verbose_name = 'Сеть'
        verbose_name_plural = 'Сети'
