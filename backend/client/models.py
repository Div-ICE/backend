from django.db import models


class Client(models.Model):
    name = models.CharField('Клиент', max_length=256, db_index=True)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self) -> str:
        return self.name


class Organization(models.Model):
    name = models.CharField('Организация', max_length=256, db_index=True)
    client_name = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='Клиент',
    )

    class Meta:
        verbose_name = 'организация'
        verbose_name_plural = 'организации'
        unique_together = ('name', 'client_name',)

    def __str__(self) -> str:
        return self.name


class Bill(models.Model):
    client_org = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='Счет',
    )
    number = models.IntegerField('№')
    sum = models.IntegerField('Сумма')
    date = models.DateField('Дата')

    class Meta:
        verbose_name = 'счет'
        verbose_name_plural = 'счета'
        unique_together = ('client_org', 'number',)

    def __str__(self) -> str:
        return self.sum
