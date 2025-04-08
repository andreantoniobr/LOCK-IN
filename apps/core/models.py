from django.db import models

# Create your models here.
class BaseModel(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Endereco(BaseModel):
    cep = models.PositiveSmallIntegerField()