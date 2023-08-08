from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=6, default="5800FF")
    description = models.CharField(max_length=500, null=True)
   # business = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)

    '''class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "business"], name="label_and_business")
        ]'''

    def __str__(self):
        return self.name
