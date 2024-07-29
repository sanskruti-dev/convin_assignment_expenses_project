import csv
from django.http import HttpResponse
from rest_framework import generics, viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from .models import User, Expense, ExpenseParticipant
from .serializers import UserSerializer, ExpenseSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RetrieveUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset

class UserExpensesListView(generics.ListAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Expense.objects.filter(user_id=user_id)

class UserExpense(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        total_expenses = ExpenseParticipant.objects.filter(user_id=user_id).aggregate(total=Sum('amount_owed'))
        return Response({'user_id': user_id, 'total_expenses': total_expenses['total']}, status=status.HTTP_200_OK)


class DownloadBalanceSheetView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        expenses = ExpenseParticipant.objects.filter(user_id=user_id)

        total_amount_owed = expenses.aggregate(total=Sum('amount_owed'))['total'] or 0

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="balance_sheet_user_{user_id}.csv"'

        writer = csv.writer(response)
        writer.writerow(['Description', 'Amount Owed', 'Percentage Owed', 'Date'])

        for expense in expenses:
            writer.writerow([
                expense.expense.description,
                expense.amount_owed,
                expense.percentage_owed,
                expense.expense.date
            ])

        writer.writerow([])
        writer.writerow(['Total Amount Owed', total_amount_owed])

        return response
