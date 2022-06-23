from dataclasses import field, fields
from unicodedata import name
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.generics import get_object_or_404

from client.models import Client, Organization, Bill


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('name',)



class BillSerializer(serializers.ModelSerializer):
    client_org = serializers.SlugRelatedField(
        queryset = Organization.objects.all(),
        slug_field='name'
    )
    sum = serializers.IntegerField()
    class Meta:
        model = Bill
        fields = ('client_org', 'sum',)



class OrganizationSerializer(serializers.ModelSerializer):
    client_name = serializers.SlugRelatedField(
        queryset=Client.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Organization
        fields = ('name', 'client_name', 'bill',)
class ClientListSerializer(serializers.ModelSerializer):
    org_name = OrganizationSerializer(many=True, read_only=True)
    bill = BillSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ('name', 'org_name', 'bill',)
        #depth = 4
