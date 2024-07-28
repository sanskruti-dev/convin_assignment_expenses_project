from rest_framework import serializers
from .models import User, Expense, ExpenseParticipant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'mobile_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ExpenseParticipantSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = ExpenseParticipant
        fields = ['user', 'amount_owed', 'percentage_owed']
        extra_kwargs = {
            'amount_owed': {'required': False},
            'percentage_owed': {'required': False},
        }

class ExpenseSerializer(serializers.ModelSerializer):
    participants = ExpenseParticipantSerializer(many=True)

    class Meta:
        model = Expense
        fields = ['id', 'user', 'description', 'amount', 'date', 'split_method', 'participants']

    def validate(self, data):
        participants = data.get('participants', [])
        if data.get('split_method') == 'percentage':
            total_percentage = sum(participant.get('percentage_owed', 0) for participant in participants)
            if total_percentage != 100:
                raise serializers.ValidationError("The total percentage owed must be 100%.")

        return data

    def create(self, validated_data):
        participants_data = validated_data.pop('participants')
        expense = Expense.objects.create(**validated_data)

        if validated_data['split_method'] == 'equal':
            total_participants = len(participants_data)
            amount_per_participant = validated_data['amount'] / total_participants
            for participant_data in participants_data:
                participant_data['amount_owed'] = amount_per_participant
                ExpenseParticipant.objects.create(expense=expense, **participant_data)
        elif validated_data['split_method'] == 'percentage':
            for participant_data in participants_data:
                if 'percentage_owed' in participant_data:
                    participant_data['amount_owed'] = (validated_data['amount'] * participant_data['percentage_owed']) / 100
                ExpenseParticipant.objects.create(expense=expense, **participant_data)

        return expense

    def update(self, instance, validated_data):
        participants_data = validated_data.pop('participants')
        instance.user = validated_data.get('user', instance.user)
        instance.description = validated_data.get('description', instance.description)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)
        instance.split_method = validated_data.get('split_method', instance.split_method)
        instance.save()

        instance.participants.all().delete()

        if validated_data['split_method'] == 'equal':
            total_participants = len(participants_data)
            amount_per_participant = validated_data['amount'] / total_participants
            for participant_data in participants_data:
                participant_data['amount_owed'] = amount_per_participant
                ExpenseParticipant.objects.create(expense=instance, **participant_data)
        elif validated_data['split_method'] == 'percentage':
            for participant_data in participants_data:
                if 'percentage_owed' in participant_data:
                    participant_data['amount_owed'] = (instance.amount * participant_data['percentage_owed']) / 100
                ExpenseParticipant.objects.create(expense=instance, **participant_data)

        return instance
