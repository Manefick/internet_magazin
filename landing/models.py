from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    # красивий вывод в админке
    # def __str__(self):
    #     return 'Имя:{}, E-mail: {}'.format(self.name, self.email)