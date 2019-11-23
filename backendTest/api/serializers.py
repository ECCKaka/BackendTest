from rest_framework import serializers
from backendTest.models import *

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.db import transaction
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    CharField,
    EmailField,
    ValidationError,
    HyperlinkedIdentityField,
    ListSerializer,
    )

# create PropertiesSerializer as ModelSerializer
class PropertiesSerializer(ModelSerializer):
    class Meta:
        # using Properties Model.
        model = Properties
        # the fields are going to show up to user
        fields = [
            "pageFrom",
            "pageTo",
            "viewedId",
            "locationX",
            "locationY",
        ]

# create PropertiesSerializer as ModelSerializer
class ActionsSerializer(ModelSerializer):
    # one to one field build in Action Model
    properties = PropertiesSerializer(required=False)
    class Meta:
        # using Actions Model
        model = Actions
        # fields are going to show up
        fields = [
            'time',
            'type',
            'properties'
        ]

class SessionSerializer(ModelSerializer):

    class Meta:
        model = Session
        fields = ['sessionId']

class UserSerializer(ModelSerializer):
    actions = ActionsSerializer(many=True, required=False)
    session = SessionSerializer(many=True, required=False)
    class Meta:
        model = User
        depth = 0
        fields = [
            'id',
            'actions',
            'session',
            ]
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
            "session": {
                "read_only": False,
                "required": False,
            },
        }
    def create(self, validated_data):
        with transaction.atomic():
            actions = validated_data.pop('actions', [])
            sessions = validated_data.pop('session',[])
            userId = validated_data.pop('id', None)
            user = User.objects.get(id = userId)
            for session in sessions:

                sessionId = Session.objects.filter(userId = user, sessionId = session['sessionId'])

                if len(sessionId) == 0:
                    Session.objects.create(userId = user, sessionId = session['sessionId'])

            for action in actions:
                actionId = Actions.objects.create(
                        time = action['time'],
                        type = action['type'],
                        user = user
                    )
                properties = action.pop('properties', [])
                if len(properties)!=0:
                    Properties.objects.create(
                        pageFrom = properties['pageFrom'],
                        pageTo = properties['pageTo'],
                        viewedId = properties['viewedId'],
                        locationX = properties['locationX'],
                        locationY = properties['locationY'],
                        actionId = actionId,
                    )
            return user
