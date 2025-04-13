from django.db import models
from apps.core.models import BaseModel, Address


# Create your models here.
class Enterprise(BaseModel):
    legal_name = models.CharField(max_length=255, verbose_name="Razão Social")
    business_name = models.CharField(
        max_length=255,
        verbose_name="Nome Fantasia"
    )
    cnpj = models.CharField(max_length=18, verbose_name="CNPJ")
    email = models.CharField(max_length=255, verbose_name="Email")
    phone = models.CharField(max_length=14, verbose_name="Numero de telefone")
    description = models.TextField(verbose_name="Descrição")
    address = models.ManyToManyField(
        Address,
        related_name="entrepises",
        verbose_name="Endereços"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"


class Card(BaseModel):
    enterpise_id = models.ForeignKey(
        Enterprise,
        on_delete=models.PROTECT,
        related_name="cards",
        verbose_name="ID da empresa"
    )
    rfid = models.CharField(max_length=8, verbose_name="RFID")
    available = models.BooleanField(default=True, verbose_name="Disponivel")

    class Meta:
        ordering = ['-created_at', 'available']
        verbose_name = "Cartão"
        verbose_name_plural = "Cartões"


class Locker(BaseModel):
    enterpise_id = models.ForeignKey(
        Enterprise,
        on_delete=models.PROTECT,
        related_name="lockers",
        verbose_name="ID da empresa"
    )
    card_id = models.ForeignKey(
        Card,
        on_delete=models.PROTECT,
        related_name="lockers",
        verbose_name="Cartão"
    )
    number = models.PositiveSmallIntegerField(verbose_name="Número do Armário")
    available = models.BooleanField(default=True, verbose_name="Disponivel")

    class Meta:
        ordering = ['-created_at', 'available']
        verbose_name = "Armário"
        verbose_name_plural = "Armários"
