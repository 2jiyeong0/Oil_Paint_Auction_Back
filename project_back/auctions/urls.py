from django.urls import path

from . import views


urlpatterns = [
    path('mypage/', views.MyPageView.as_view(), name='mypage_view'),
    path('',views.AuctionAlllistView.as_view(), name='auction_list_view'),
    path('detail/<int:auction_id>/',views.AuctionDetailView.as_view(), name='auction_detail_view'),    
    path('<int:painting_id>/', views.AuctionListView.as_view(), name='auction_list_view'),
    path('<int:auction_id>/likes/',views.LikeView.as_view(), name="like_view"),
]