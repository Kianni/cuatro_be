import re

from django.db import models

class Sequence(models.Model):
    name = models.CharField(max_length=100)
    first_term = models.IntegerField()
    expression = models.CharField(max_length=100)

    def generate_first_seven_terms(self):
        terms = []  # Create an empty list to store the terms

        if self.meets_conditions(self.expression):
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

    def meets_conditions(self, input_string):
        # Define a regex pattern to match the conditions
        pattern = r'a1.*n'  # Check for "a1" and "n" in the string

        # Use a regex pattern to find all matches in the input string
        matches = re.findall(pattern, input_string)

        # Check if there's at least one match and the input string contains only valid characters
        if matches and all(char in '0123456789+-*/()' for char in re.sub(pattern, '', input_string)):
            return True
        else:
            return False
