from dataclasses import fields
from pyexpat import model

from rest_framework import serializers
from . import models

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ('name', 'description','members')


class GroupmemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroupMember
        fields = ('group', 'user')

