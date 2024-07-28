from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from expenses.views import CreateUserView, DownloadBalanceSheetView, RetrieveUserView, UserExpense, UserViewSet, ExpenseViewSet, UserExpensesListView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('users/', CreateUserView.as_view(), name='create_user'),
    path('users/<int:pk>/', RetrieveUserView.as_view(), name='retrieve_user'),
    path('api/expenses/user/<int:user_id>/', UserExpense.as_view(), name='participant-total-expenses'),
    path('api/expenses/user/<int:user_id>/download/', DownloadBalanceSheetView.as_view(), name='download-balance-sheet'),
]
