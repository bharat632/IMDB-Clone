from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stream import views

router = DefaultRouter()
router.register('reviews', views.ReviewsVS , basename='reviews')

urlpatterns = [
    path('stream/',views.StreamAV.as_view(), name = 'streams'),
    path('stream/<int:pk>',views.StreamDetailsAV.as_view(), name = 'stream-details'),

    path('shows/', views.ShowsAV.as_view(), name= 'shows'),
    path('shows/<int:pk>', views.ShowDetailsAV.as_view(), name = 'show-details'),
    path('shows/<int:pk>/review/', views.ShowReviewsAV.as_view(), name = 'show-reviews'),

    path('', include(router.urls))
    # path('reviews/<int:pk>', views.ReviewDetailsAV.as_view(), name= 'review-details'),
    
]
