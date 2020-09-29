from django.db import models

# Create your models here.

class Brand(models.Model):
    brand = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.brand

    class Meta:
        ordering = ['brand']


class ValveType(models.Model):
    valve_type = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.valve_type

    class Meta:
        ordering = ['valve_type']


class BellSize(models.Model):
    bell_size = models.DecimalField('bell size (inches)', max_digits=3, decimal_places=1, primary_key=True)

    def __str__(self):
        return str(self.bell_size)

    class Meta:
        ordering = ['bell_size']


class BellMaterial(models.Model):
    bell_material = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.bell_material

    class Meta:
        ordering = ['bell_material']


class Finish(models.Model):
    finish = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.finish

    class Meta:
        ordering = ['finish']
        verbose_name_plural = "finishes"


class OuterSlideMaterial(models.Model):
    outer_slide_material = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.outer_slide_material

    class Meta:
        ordering = ['outer_slide_material']


class BassTrombone(models.Model):
    NUMBER_OF_VALVES_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
    ]
    VALVE_CONFIGURATION_CHOICES = [
        ('Not applicable', 'Not applicable'),
        ('Dependent', 'Dependent'),
        ('Independent', 'Independent'),
    ]
    WRAP_CHOICES = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    ]
    DUAL_BORE_CHOICES = [
        ('Dual bore', 'Dual bore'),
        ('Not dual bore', 'Not dual bore'),
    ]
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    model = models.CharField(max_length=50)
    number_of_valves = models.CharField(max_length=6, choices=NUMBER_OF_VALVES_CHOICES)
    valve_configuration = models.CharField(max_length=14, choices=VALVE_CONFIGURATION_CHOICES)
    valve_type = models.ForeignKey(ValveType, on_delete=models.PROTECT)
    wrap = models.CharField(max_length=6, choices=WRAP_CHOICES)
    bell_size = models.ForeignKey(BellSize, on_delete=models.PROTECT)
    bell_material = models.ForeignKey(BellMaterial, on_delete=models.PROTECT)
    dual_bore = models.CharField(max_length=13, choices=DUAL_BORE_CHOICES)
    finish = models.ForeignKey(Finish, on_delete=models.PROTECT)
    outer_slide_material = models.ForeignKey(OuterSlideMaterial, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.brand) + " " + self.model

    class Meta:
        ordering = ['brand', 'model']


class CustomizableBassTrombone(models.Model):
    bass_trombone = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.bass_trombone

    class Meta:
        ordering = ['bass_trombone']
