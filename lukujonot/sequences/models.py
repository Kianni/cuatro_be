from django.db import models

class Sequence(models.Model):
    name = models.CharField(max_length=100)
    first_term = models.IntegerField()
    expression = models.CharField(max_length=100)

    def generate_first_seven_terms(self):
        terms = [str(eval(self.expression.replace('n', str(n))) for n in range(1, 8))]
        return ', '.join(terms)

    def __str__(self):
        return self.name
