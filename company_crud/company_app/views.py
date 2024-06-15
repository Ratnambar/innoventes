from django.shortcuts import render

# Create your views here.

from .models import Company
from rest_framework import viewsets # type: ignore
from .serializers import CompanySerializer
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1


class CompanyViewSet(viewsets.ViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request):
        page_query_param = 'page'
        paginator = PageNumberPagination()
        paginator.page_size = 1
        paginator.page_query_param = page_query_param
        qry_set = Company.objects.all()
        p = paginator.paginate_queryset(queryset=qry_set, request=request) # change 1
        serializer = CompanySerializer(p, many=True) # change 2
        theData= serializer.data
        return paginator.get_paginated_response(theData) # change 3


    def create(self, request):
        data = request.data
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"messages":"company created."})
        print(serializer.data)
        return Response({"message":serializer.errors})
        

    def retrieve(self, request, pk=None):
        company = Company.objects.get(id=int(pk))
        if company:
            serializer = CompanySerializer(company) 
            print(serializer.data)
            return Response({"messages":serializer.data})
        return Response({"message":"company not eist"})


    def update(self, request, pk=None):
        company = Company.objects.get(id=pk)
        if company:
            company.company_name = request.data['company_name']
            company.email = request.data['email']
            company.company_code = request.data['company_code']
            company.strength = request.data['strength']
            company.web_site = request.data['web_site']
            company.save()
            return Response({"message":"data updated"})
        return Response({"message":"not updated"})


    def destroy(self, request, pk=None):
        company = Company.objects.get(id=pk)
        if company:
            company.delete()
            return Response({"message":"record deleted"})
        return Response({"message":"record alreday deleted"})
