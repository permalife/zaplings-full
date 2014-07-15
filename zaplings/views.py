from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from zaplings.models import FeaturedIdea, Love, Offer, Need, UserLove, NewUserEmail
from django.template import RequestContext, loader
from django.views import generic
import time
#def index(request):
    #latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = RequestContext(request, {
    #    'latest_poll_list': latest_poll_list,
    #})
    #context = {'latest_poll_list': latest_poll_list}
    #return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context))
    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the poll index.")
class SignupView(generic.ListView):
    model = User
    template_name = 'zaplings/signup.html'

    #def get_queryset(self):
    #    """Return the last five published polls."""
    #    return Poll.objects.order_by('-pub_date')[:5]

class ProfileView(generic.ListView):
    model = User
    template_name = 'zaplings/profile.html'

    #def get_queryset(self):
    #    """Return the last five published polls."""
    #    return Poll.objects.order_by('-pub_date')[:5]

class AboutView(generic.ListView):
    model = User
    template_name = 'zaplings/10-reasons.html'
    
class HowItWorksView(generic.ListView):
    model = User
    template_name = 'zaplings/howitworks.html'
    
class GetInvolvedView(generic.ListView):
    model = User
    template_name = 'zaplings/getinvolved.html'
    
class FaqView(generic.ListView):
    model = User
    template_name = 'zaplings/faq.html'

class LovesView(generic.ListView):
    template_name = 'zaplings/loves.html'
    context_object_name = 'suggested_loves'

    def get_queryset(self):
        """Return the all suggested loves."""
        return Love.objects.all()
    
class RecordLovesView(generic.ListView):
    template_name = 'zaplings/record_loves.html'
    context_object_name = 'selected_loves'
    
class RecordNewEmailView(generic.ListView):
    model = User    
    template_name = 'zaplings/index.html'
    
class IdeaFeedView(generic.ListView):
    model = User    
    template_name = 'zaplings/idea-feed.html'

class EditProfileView(generic.ListView):
    model = User
    template_name = 'zaplings/editprofile.html'
    
class ViewIdeaPageView(generic.ListView):
    model = User
    template_name = 'zaplings/view-idea-page.html'

class EditIdeaPageView(generic.ListView):
    model = User
    template_name = 'zaplings/edit-idea-page.html'

class ShareView(generic.ListView):
    model = User
    template_name = 'zaplings/share.html'
 
class ProfileTextView(generic.ListView):
    model = Love
    template_name = 'zaplings/profile-text.html'

class IndexView(generic.ListView):
    #model = FeaturedIdea
    template_name = 'zaplings/index.html'
    context_object_name = 'featured_ideas'

    def get_queryset(self):
        """Return the all features ideas."""
        return FeaturedIdea.objects.all()

#def detail(request, poll_id):
    #poll = Poll.objects.get(id=poll_id)
    #context = {'poll': poll}
    #return render(request, 'polls/detail.html', context)
    #return HttpResponse("You're looking at poll %s." % poll_id)

#def results(request, poll_id):
    #poll = get_object_or_404(Poll, pk=poll_id)
    #return render(request, 'polls/results.html', {'poll': poll})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

    #return HttpResponse("You're voting on poll %s." % poll_id)

def record_loves(request):
    if request.method == "POST":
        print "request is POST"
        selected_loves = request.POST.getlist("love_tag")
    else:
        print "request is not POST"
        selected_loves = ["NOT POST"]
    print selected_loves

    return render(request, 'zaplings/profile-text.html', {
    'selected_loves': selected_loves
    })

def record_new_email(request):
    email = request.POST['email']
    status_message = None
    if not email or email == "" or not '@' in email:
        status_message = "Please double-check the email field."
    elif NewUserEmail.objects.filter(email=email):
        status_message = "This email has already been submitted."
    else:
        NewUserEmail.objects.create(email=email)
        status_message = "Thanks, your email has been recorded!"
    
    return render(request, 'zaplings/index.html', {
        'status_message': status_message,
        'featured_ideas': FeaturedIdea.objects.all()
    })

def login(request):
    error_message = None
    try:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                success_message = "User %s is valid, active and authenticated"
            else:
                success_message = "The password is valid, but the account %s has been disabled!"
        else:
            # the authentication system was unable to verify the username and password
            error_message = "The username and password were incorrect."

    except (KeyError, User.DoesNotExist):
        # Redisplay the poll voting form.
        error_message = "Please include both email and password."

    if '@' not in email or len(email.split('.')) == 1:
        error_message = "Are you serious? What kind of email is this: %s?" % email

    if error_message:
        return render(request, 'zaplings/signup.html', {
            'error_message': error_message,
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        #p = get_object_or_404(User, pk=user_id)
        #return HttpResponse(success_message % email)
        
        return render(request, 'zaplings/profile-love.html', {
            'username': user.get_username(),
            'user': user
        })

        #return HttpResponseRedirect(reverse('polls:profile', args=(user.id,)))


