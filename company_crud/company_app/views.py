from django.shortcuts import render

# Create your views here.

from .models import Company
from rest_framework import viewsets, status # type: ignore
from .serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class CompanyViewSet(viewsets.ViewSet):
    pagination_class = StandardResultsSetPagination

    def list(self, request):
        paginator = self.pagination_class()
        queryset = Company.objects.all()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = CompanySerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request):
        data = request.data
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"messages":"company created."})
        return Response({"message":serializer.errors})
        

    def retrieve(self, request, pk=None):
        try:
            company = Company.objects.get(id=int(pk))
        except Company.DoesNotExist:
            return Response({"message":status.HTTP_404_NOT_FOUND})
        serializer = CompanySerializer(company) 
        return Response({"messages":serializer.data})


    def update(self, request, pk=None):
        try:
            company = Company.objects.get(id=pk)
        except Company.DoesNotExist:
            return Response({"message":status.HTTP_404_NOT_FOUND})
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"data updated"})
        return Response({"message":serializer.errors})


    def destroy(self, request, pk=None):
        try:
            company = Company.objects.get(id=pk)
        except Company.DoesNotExist:
            return Response({"message":status.HTTP_404_NOT_FOUND})
        company.delete()
        return Response({"message":"record deleted"})