from django.core.exceptions import ValidationError
from datetime import date


def validate_weekday(value):
        if value.weekday() == 5 or value.weekday() == 6:
            raise ValidationError(f"Sorry we work from monday to friday.")