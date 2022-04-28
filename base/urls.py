from django.urls import path
from . views import TaskList ,DetailsView,TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, Logout, RegisterForm

urlpatterns = [
    path('register/',RegisterForm.as_view(),name="register"),
    path('login/',CustomLoginView.as_view(), name="login"),
    path('logout/',Logout.as_view(),name="logout"),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',DetailsView.as_view(), name="DetailsView"),
    path('task-create',TaskCreate.as_view(),name = "task-create"),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name="task-update"),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name="task-delete"),
   
]