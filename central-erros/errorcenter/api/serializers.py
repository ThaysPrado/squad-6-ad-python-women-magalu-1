from rest_framework import serializers
from .models import Log, Origin, User

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['title',
                  'details',
                  'number_events',
                  'occurrence_date',
                  'active',
                  #environment
                  #level
                  #origin
                  #user
                 ]
        read_only_fields = ['occurrence_date', 'active']

class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = ['description']
        read_only_fields = ['description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'last_login']
        read_only_fields = ['last_login']
    