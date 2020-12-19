from rest_framework import serializers
from .models import User, Class, Race, Character

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'date_created')


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'title', 'description')


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ('id', 'title', 'description', 'bonuses')


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'full_name', 'age', 'back_story', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'equipment', 'spells', 'race_id', 'class_id', 'user_id')


