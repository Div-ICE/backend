from dataclasses import field, fields
from pyexpat import model
from unicodedata import name
from backend.xlsx import create_list, read_xlsx
from django import views
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from drf_multiple_model.views import ObjectMultipleModelAPIView


from .serializers import (BillSerializer, ClientSerializer,
                         OrganizationSerializer, ClientListSerializer)
from client.models import Client, Organization, Bill


class FileUploadView(APIView):

    def post(self, request, filename):
        file_obj = request.data['file']

        if str(file_obj) == 'client_org.xlsx':
            sheet_client, rows, cols = read_xlsx(file_obj, 'client')
            sheet_org, rows, cols = read_xlsx(file_obj, 'organization')

            list_client = create_list(sheet_client, rows, cols)
            for item in list_client:

                serializer = ClientSerializer(data=item)
                if serializer.is_valid(raise_exception=True):
                    name = serializer.validated_data['name']
                    serializer.save()

            list_org = create_list(sheet_org, rows, cols)
            for item in list_org:
                serializer = OrganizationSerializer(data=item)
                if serializer.is_valid(raise_exception=True):
                    client_name = serializer.validated_data['client_name']
                    name = serializer.validated_data['name']
                    serializer.save()

            print(list_client)
            print(list_org)
            return Response(status=200)
        if str(file_obj) == 'bills.xlsx':
            sheet_bills, rows, cols = read_xlsx(file_obj, 'Лист1')
            list_bills = create_list(sheet_bills, rows, cols)
            for item in list_bills:
                serializer = BillSerializer(data=item)
                print(item)
                if serializer.is_valid(raise_exception=True):
                    client_org = serializer.validated_data['client_org']
                    number = serializer.validated_data['number']
                    sum = serializer.validated_data['sum']
                    date = serializer.validated_data['date']
                    serializer.save()
            print(list_bills)
            return Response(status=200)
        else:
            return Response(status=415)

class ClientViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()
    class Meta:
        model = Client
        fields = ('name', 'client_name_id',)

class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    class Meta:
        model = Organization
        fields = ('name', 'client_name', 'bill',)


class BillViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()

    class Meta:
        model = Bill
        fields = ('client_org', 'number', 'sum', 'date',)