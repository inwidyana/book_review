from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="review.index"),

    path('book/<int:book_id>', views.book, name="review.book"),

    path('login', views.signin, name="review.login"),
    path('attempt_login', views.signin, name="review.loginAttempt"),

    path('register', views.register, name="review.register"),
    path('attempt_register', views.register, name="review.registerAttempt"),

    path('logout', views.signout, name="review.logout"),
]