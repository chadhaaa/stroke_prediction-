from django.db import models

class PredResults(models.Model):
    gender = models.FloatField()
    age = models.FloatField()
    hypertension = models.FloatField()
    heart_disease = models.FloatField()
    ever_married = models.FloatField()
    work_type = models.FloatField()
    residence_type = models.FloatField()
    avg_glucose_level = models.FloatField()
    bmi = models.FloatField()
    smoking_status = models.FloatField()
    

    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification

