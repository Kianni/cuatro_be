from django.db import models

class Sequence(models.Model):
    name = models.CharField(max_length=100)
    first_term = models.IntegerField()
    expression = models.CharField(max_length=100)

    def generate_first_seven_terms(self):
        terms = []  # Create an empty list to store the terms

        for n in range(1, 8):
            expression_with_substitution = self.expression.replace('n', str(n))
            expression_with_substitution = self.expression.replace('a1', str(self.first_term))

            # Evaluate the modified expression and convert the result to a string
            term = str(eval(expression_with_substitution))

            # Append the result to the list of terms
            terms.append(term)

        return terms

    def __str__(self):
        return self.name
