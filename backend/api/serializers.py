from client.models import Bill, Client, Organization
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('name',)


class BillSerializer(serializers.ModelSerializer):
    client_org = serializers.SlugRelatedField(
        queryset=Organization.objects.all(),
        slug_field='name'
    )
    sum = serializers.IntegerField()

    class Meta:
        model = Bill
        fields = ('client_org', 'sum',)
        exclude = ('id',)


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
