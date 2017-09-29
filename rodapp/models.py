from django.db import models
from django.contrib.auth.models import User

class Feature(models.Model):
    name = models.CharField(max_length=45)
    calculations = models.CharField(max_length=500, null=True)
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)

    class Meta:
        db_table = 'features'


class Symbol(models.Model):
    name = models.CharField(max_length=45, null=True)
    url = models.CharField(max_length=500, null=True)
    api_url = models.CharField(max_length=500, null=True)
    api_key = models.CharField(max_length=45, null=True)
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)

    class Meta:
        db_table = 'symbols'


class Algorithm(models.Model):
    name = models.CharField(max_length=45, null=True)
    api_url = models.CharField(max_length=500, null=True)
    api_key = models.CharField(max_length=45, null=True)
    desc = models.CharField(max_length=500, null=True)
    param = models.CharField(max_length=45, null=True)
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)

    class Meta:
        db_table = 'algorithms'


class Prediction(models.Model):
    name = models.CharField(max_length=45, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    period = models.IntegerField()
    percentage = models.DecimalField(max_digits=2, decimal_places=0)
    result = models.IntegerField()
    actual = models.IntegerField()
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)

    symbol = models.ManyToManyField(Symbol, db_table='xpredictionsymbol')
    feature = models.ManyToManyField(Feature, db_table='xpredictionfeature')
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'predictions'