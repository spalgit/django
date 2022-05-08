from django.urls import path, reverse_lazy
from . import views

app_name='unesco'
urlpatterns = [
    path('', views.RegionView.as_view(), name='all'),
    # path('site/<int:site_id>', views.SiteView.as_view(), name='site_list'),
    # path('site_list/<int:pk>', views.getsite, name='site_list'),
    path('site/<int:region_id>', views.SiteDetailView.as_view(), name='site_list'),
    # path('ad/creat
    #     views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_create'),
    # path('ad/<int:pk>/update',
    #     views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_update'),
    # path('ad/<int:pk>/delete',
    #     views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_delete'),
]
