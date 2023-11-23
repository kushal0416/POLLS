from .models import Poll, Choice, Vote,User
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# ...
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        def create(self, validated_data):
            user = User(
            email=validated_data['email'],
            username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            Token.objects.create(user=user)
            return user

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)
    class Meta:
        model = Choice
        fields = '__all__'
class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Poll
        fields = '__all__'



# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'

#     def is_valid(self, raise_exception=False):
#         valid = super().is_valid(raise_exception=raise_exception)
#         if not valid:
#             return False

#         # Additional custom validation logic
#         if self.validated_data.get('publication_date') < timezone.now().date():
#             self.errors['publication_date'] = ['Publication date cannot be in the past.']
#             return False

#         return True

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'

#     def save(self, **kwargs):
#         instance = super().save(**kwargs)
#         # Additional custom save logic
#         if not instance.is_published:
#             instance.is_published = True
#             instance.save()
#         return instance
