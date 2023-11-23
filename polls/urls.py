from django.urls import path
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, UserCreate,LoginView

urlpatterns = [

path("users/", UserCreate.as_view(), name="user_create"),
path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
path("login/",LoginView.as_view(), name="login"),
]