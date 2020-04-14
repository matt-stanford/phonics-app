from django.db import models

class Card(models.Model):
    card_image = models.ImageField(upload_to='images/')
    card_word = models.CharField(max_length=10)

    def __str__(self):
        return self.card_word

    objects = models.Manager()
