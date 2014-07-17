from django.conf.urls import patterns, url

from zaplings import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^$', views.RecordNewEmailView.as_view(), name='record_new_email'),    
    url(r'^(?P<pk>\d+)/profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^10-reasons/$', views.AboutView.as_view(), name='10-reasons'),
    url(r'^howitworks/$', views.HowItWorksView.as_view(), name='howitworks'),
    url(r'^getinvolved/$', views.GetInvolvedView.as_view(), name='getinvolved'),
    url(r'^faq/$', views.FaqView.as_view(), name='faq'),
    url(r'^loves/$', views.LovesView.as_view(), name='loves'),
    url(r'^offers/$', views.OffersView.as_view(), name='offers'),
    url(r'^needs/$', views.NeedsView.as_view(), name='needs'),
    url(r'^idea-feed/$', views.IdeaFeedView.as_view(), name='idea-feed'),
    url(r'^comments/$', views.CommentsView.as_view(), name='comments'),
    url(r'^record_loves/$', views.record_loves, name='record_loves'),
    url(r'^view-idea-page/$', views.ViewIdeaPageView.as_view(), name='view-idea-page'),
    url(r'^edit-idea-page/$', views.EditIdeaPageView.as_view(), name='edit-idea-page'),
    url(r'^editprofile/$', views.EditProfileView.as_view(), name='editprofile'),
    url(r'^share/$', views.ShareView.as_view(), name='share'),    
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    #url(r'^(?P<user_id>\d+)/login/$', views.login, name='login'),
    url(r'^record_new_email/$', views.record_new_email, name='record_new_email'),
    url(r'^profile-text/$', views.ProfileTextView.as_view(), name='profile-text'),
    url(r'^login/$', views.login, name='login')  
)
