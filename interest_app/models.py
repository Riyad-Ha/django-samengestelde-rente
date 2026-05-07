from django.db import models

class Berekening(models.Model):
    kapitaal = models.FloatField()
    rente = models.FloatField()
    looptijd = models.FloatField()
    eindbedrag = models.FloatField()
    rentewinst = models.FloatField()
    datum_berekening = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Berekening van {self.datum_berekening:%Y-%m-%d %H:%M} : €{self.eindbedrag:.2f}"