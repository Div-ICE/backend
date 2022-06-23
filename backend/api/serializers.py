from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from client.models import Client, Organization, Bill


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('name',)


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('name', 'client_name',)


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ('client_org', 'number', 'sum', 'date',)
