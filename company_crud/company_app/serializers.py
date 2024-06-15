from .models import Company
from rest_framework import serializers



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


    def create(self, validate_data):
        return Company.objects.create(**validate_data)
        # return company