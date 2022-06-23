from backend.xlsx import create_list, read_xlsx
from django import views
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (BillSerializer, ClientSerializer,
                         OrganizationSerializer)


class FileUploadView(APIView):

    def post(self, request, filename):
        file_obj = request.data['file']

        if str(file_obj) == 'client_org.xlsx':
            sheet_client, rows, cols = read_xlsx(file_obj, 'client')
            sheet_org, rows, cols = read_xlsx(file_obj, 'organization')

            list_client = create_list(sheet_client, rows, cols)
            for item in list_client:

                serializer = ClientSerializer(data=item)
                print(item)
                if serializer.is_valid():
                    serializer.save()

            list_org = create_list(sheet_org, rows, cols)
            for item in list_org:
                serializer = OrganizationSerializer(data=item)
                print(item)
                if serializer.is_valid():
                    serializer.save()

            print(list_client)
            print(list_org)
        if str(file_obj) == 'bills.xlsx':
            sheet_bills, rows, cols = read_xlsx(file_obj, 'Лист1')
            list_bills = create_list(sheet_bills, rows, cols)
            for item in list_bills:
                serializer = BillSerializer(data=item)
                print(item)
                if serializer.is_valid:
                    serializer.create()
            print(list_bills)
        else:
            return Response(status=415)

        return Response(status=200)

