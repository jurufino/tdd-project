from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.text == '':
            raise Exception("Você não pode enviar um item vazio")
        super().save(*args, **kwargs)