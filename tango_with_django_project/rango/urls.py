from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^about/', views.about, name='about'),
            url(r'^add_category/$', views.add_category, name='add_category'),
            url(r'^delete_workExperience/(?P<id>\d+)/', views.delete_workExperience, name='delete_workExperience'),
            url(r'^delete_education/(?P<id>\d+)/', views.delete_education, name='delete_education'),
            url(r'^save_workExperience/(?P<id>\d+)/', views.save_workExperience, name='save_workExperience'),
            url(r'^save_education/(?P<id>\d+)/', views.save_education, name='save_education'),
            url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
            url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
            url(r'^restricted/', views.restricted, name='restricted'),
            url(r'^search/', views.search, name='search'),
            url(r'^goto/', views.track_views, name='goto'),
            url(r'^add_profile/', views.register_profile, name='add_profile'),
            url(r'^profile/', views.profile, name='profile'),
            url(r'^pub-profile/(?P<id>\d+)/', views.pubProfile, name='pubProfile'),
            url(r'^users/', views.xpusers, name='users'),
            url(r'^paintings/', views.paintings, name='paintings'),
            url(r'^like_category/$', views.like_category, name='like_category'),
            url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
            url(r'^auto_add_page/$', views.auto_add_page, name='auto_add_page'),
            url(r'^group/$', views.group, name='group'),
            url(r'^send_email/(?P<id>\d+)/', views.send_email, name='send_email'),
            url(r'^accept_invite/(?P<id>\d+)/', views.accept_invite, name='send_email'),
            #url(r'^leave_group/(?P<id>\d+)/', views.leave_group, name='leave_group'),
            #url(r'^join_group/(?P<id>\d+)/', views.join_group, name='join_group'),
            url(r'^no_user/$', views.no_user, name='no_user'),
            url(r'^user_login/$', views.user_login, name='user_login'),
            url(r'^ajax_user_search/', views.ajax_user_search, name='ajax_user_search'),
            url(r'^cookies/$', views.cookies, name='cookies'),
            
           
            )

