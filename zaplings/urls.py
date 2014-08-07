from django.conf.urls import patterns, url

from zaplings import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^profile/(?P<pk>\d+)/$', views.ProfileView.as_view(), name='user_tags'),
    #url(r'^(?P<pk>\d+)/profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^10-reasons/$', views.AboutView.as_view(), name='10-reasons'),
    url(r'^howitworks/$', views.HowItWorksView.as_view(), name='howitworks'),
    url(r'^getinvolved/$', views.GetInvolvedView.as_view(), name='getinvolved'),
    url(r'^faq/$', views.FaqView.as_view(), name='faq'),
    url(r'^loves/$', views.LovesView.as_view(), name='loves'),
    url(r'^offers/$', views.OffersView.as_view(), name='offers'),
    url(r'^needs/$', views.NeedsView.as_view(), name='needs'),
    url(r'^where/$', views.WhereView.as_view(), name='where'),
    url(r'^when/$', views.WhenView.as_view(), name='when'),
    url(r'^idea-feed/$', views.IdeaFeedView.as_view(), name='idea-feed'),
    url(r'^discuss/$', views.DiscussView.as_view(), name='discuss'),
    url(r'^record_loves/$', views.record_loves, name='record_loves'),
    url(r'^(?P<userid>\d+)/generate_user_tags/$', views.generate_user_tags, name='generate_user_tags'),
    url(r'^record_offers/$', views.record_offers, name='record_offers'),
    url(r'^record_needs/$', views.record_needs, name='record_needs'),
    url(r'^record_wheres/$', views.record_wheres, name='record_wheres'),
    url(r'^record_whens/$', views.record_whens, name='record_whens'),
    url(r'^view-idea-page/$', views.ViewIdeaPageView.as_view(), name='view-idea-page'),
    url(r'^edit-idea-page/$', views.EditIdeaPageView.as_view(), name='edit-idea-page'),
    url(r'^editprofile/$', views.EditProfileView.as_view(), name='editprofile'),
    url(r'^share/$', views.ShareView.as_view(), name='share'),    
    url(r'^error/$', views.ErrorView.as_view(), name='error'),    
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    #url(r'^(?P<user_id>\d+)/login/$', views.login, name='login'),
    url(r'^record_new_email/$', views.record_new_email, name='record_new_email'),
    url(r'^record_text/$', views.record_text, name='record_text'),
    url(r'^signup_user/$', views.signup_user, name='signup_user'),
    url(r'^login_email_password/$', views.login_email_password, name='login_email_password'),
    url(r'^profile-text/$', views.ProfileTextView.as_view(), name='profile-text'),
    url(r'^profile-view/$', views.ViewProfileView.as_view(), name='profile-view'),
    url(r'^when/$', views.WhereView.as_view(), name='when'),
    url(r'^where/$', views.WhereView.as_view(), name='where'),
    url(r'^logout/$', views.user_logout, name='user_logout')
    #url(r'^profile-view-html-only/$', views.ViewProfileHtmlView.as_view(), name='profile-view-html-only'),
)
