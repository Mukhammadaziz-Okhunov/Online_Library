from django.db import models

class Kitob(models.Model):
    Choices = (
        ('Ilmiy', 'Ilmiy'),
        ('Badiiy', 'Badiiy'),
        ('Hujjatli', 'Hujjatli')
    )
    nom = models.CharField(max_length=30)
    sahifa = models.PositiveSmallIntegerField()
    tur = models.CharField(max_length=20, choices=Choices)
    def __str__(self):
        return f"{self.nom}, {self.tur}"

class Muallif(models.Model):
    J = (
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol")
    )
    ism = models.CharField(max_length=20)
    yosh = models.PositiveSmallIntegerField()
    jins = models.CharField(max_length=10, choices=J)
    def __str__(self):
        return f"{self.ism}"

class Record(models.Model):
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    vaqt = models.DateField()