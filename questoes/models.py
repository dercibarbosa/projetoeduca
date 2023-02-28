from django.db import models
from django.utils import timezone

class QuestoesModel(models.Model):
    questoes = models.CharField(max_length=200, null=True)
    opcao1 = models.CharField(max_length=200, null=True)
    opcao2 = models.CharField(max_length=200, null=True)
    opcao3 = models.CharField(max_length=200, null=True)
    opcao4 = models.CharField(max_length=200, null=True)
    respostaCorreta= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.questoes


