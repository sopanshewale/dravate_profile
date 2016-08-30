from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import PasswordChangeForm
from forms import UserForm, ProfileForm
from models import Userprofile
from django.contrib.auth.models import User

@login_required(login_url='/login')
def profile(request):
     user_profile = _get_profile(request)
     if user_profile:
        return render(request, 'user_profile.html',
                      {'user_profile': user_profile})
     else:
        raise Http404


@login_required(login_url='/login')
def profile_form(request):
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('/accounts/profile')


        user = User.objects.get(username=request.user.username)
        #post = request.POST.copy() # To keep Email Read-Only 
        #post['email'] = user.email
        # and update original POST in the end
        #request.POST = post

        user_form  = UserForm(request.POST, instance=user)
        if user_form.is_valid():
             user_form.save()
             try:
                 profile_instance  = Userprofile.objects.get(user_id=user.id)
             except Userprofile.DoesNotExist:
                 profile_instance = Userprofile(user_id=user.id)

             user_profile_form =  ProfileForm(request.POST, instance=profile_instance)
             if user_profile_form.is_valid():
                   user_profile_form.save()
             return redirect('/accounts/profile')
    else:

        user_profile = _get_profile(request)
        print user_profile
        user_form = \
            UserForm(initial={'first_name': user_profile['first_name'],
                     'last_name': user_profile['last_name'], 'email':user_profile['email']})
        phone = ''
        address = ''
        if 'phone' in user_profile:
             phone = user_profile['phone']
        if 'address' in user_profile:
             address = user_profile['address']

        user_profile = \
            ProfileForm(initial={'phone': phone, 'address': address, } )
        return render(request, 'profile_form.html',
                      {'user_form': user_form,
                      'user_profile': user_profile,},
                     )

def _get_profile(request):
    user_profile = {}
    if request.user.is_authenticated():
        username = request.user.username
        u = User.objects.get(username=username)
        user_profile = {'first_name': u.first_name,
                        'last_name': u.last_name, 'email': u.email}
        u_profile_model = None
        try:
            u_profile_model = Userprofile.objects.get(user_id=u.id)
        except ObjectDoesNotExist:
            u_profile_model = Userprofile()

        if u_profile_model:
            user_profile['phone'] = u_profile_model.phone
            #user_profile['phone'] = 11
            user_profile['address'] = u_profile_model.address

        return user_profile
    else:
        return None

                 

