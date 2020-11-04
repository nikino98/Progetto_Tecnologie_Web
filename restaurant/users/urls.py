
from django.urls import path
from django.contrib.auth import views as auth_views
from restaurant import views
from users.views import create_user, table_reserved, profile_view, create_takeaway, takeaway_redirect, review_list, \
    review_create_ajax, comment_create, comment_list, UpdateUser, delete_prenotazione

app_name = 'users'

urlpatterns = [
    path('create_user/', create_user.as_view(), name='user-creation'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='user-profile'),
    path('reservation/', table_reserved, name='table-reserve'),
    path('takeaway/', create_takeaway, name='takeaway'),
    path('takeaway_redirect/<str:total>/<str:food_list>/<str:drink_list>', takeaway_redirect, name='takeaway-redirect'),
    path('reviews/', review_list, name='review-list'),
    path('review_create/', review_create_ajax, name='review-create'),
    path('comment_create/<int:review_pk>', comment_create, name='comment-create'),
    path('comment_list/<int:review_pk>', comment_list, name='comment-list'),
    path('profile/modify/<int:id>', UpdateUser.as_view(), name='profile-update'),
    path('prenotazione_delete/', delete_prenotazione, name='prenotazione-delete')

]
