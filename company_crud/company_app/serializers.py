from .models import Company
from rest_framework import serializers
import re


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def validate_company_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Company should contain at least 5 characters.')
        return value
    
    def validate_company_code(self, value):
        pattern = r"^[A-Za-z]{2}\d{2}[EN]$"
        if not re.match(pattern, value):
            errors = []
            if len(value) != 5:
                errors.append('Length should be 5 characters.')
            if not re.match(r"^[A-Za-z]{2}", value[:2]):
                errors.append('1st & 2nd characters should be alphabets.')
            if not re.match(r"\d{2}", value[2:4]):
                errors.append('3rd & 4th characters should be numbers.')
            if not re.match(r"[EN]$", value[4]):
                errors.append('5th character should be E or N.')

            if errors:
                raise serializers.ValidationError(errors)
        return value

    def validate_strength(self, value):
        if value > 0 or value == 0:
            return value
        raise serializers.ValidationError("Strngth should be zero or grater than zero.")
   

    def create(self, validate_data):
        return Company.objects.create(**validate_data)