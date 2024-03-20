from django.shortcuts import render, redirect
from  lynxe.forms import CreateUserForm, LoginFrom, UpdateUserForm, UpdateProfileForm


from . models import profile


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




def index1(request):
    return render(request, 'lynx/index.html')

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():

            current_user = form.save(commit=False)

            form.save()

            profile1 = profile.objects.create(user=current_user)

            

            return redirect("my-login")
        
    context = {'form': form}


    return render(request, 'lynx/register.html', context=context)

def my_login(request):

    forms = LoginFrom()
    form = LoginFrom(request, data=request.POST)

    if request.method == 'POST':
        #form = LoginFrom(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('dasboard')
    context = {'form': form}       
    


    return render(request, 'lynx/my-login.html', context=context )

def user_logout(request):

    auth.logout(request)

    return redirect("")
    

    
@login_required(login_url='my-login')
def dasboard(request):

    profile_pic =profile.objects.get(user=request.user)

    context = {'profile_pic': profile_pic}




    return render(request, 'lynx/dasboard.html', context=context)

@login_required(login_url='my-login')
def profile_management(request):

    user_form = UpdateUserForm(instance=request.user)

    Profile = profile.objects.get(user=request.user)

    profile_form = UpdateProfileForm(instance = Profile)

    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)

        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=Profile)

        if user_form.is_valid():
            user_form.save()
            return redirect("dasboard")
        

        if profile_form.is_valid():

            profile_form.save()

            return redirect("dasboard")
        
        
    context = {'user_form':user_form, 
               'profile_form': profile_form,
               }


   



    return render(request, 'lynx/profile.management.html', context=context)


@login_required(login_url='my-login')
def delete_account(request):
    if request.method == "POST":
        deleteUser = User.objects.get(username=request.user)
        deleteUser.delete()

        return redirect("")
    
    return render(request, 'lynxe/delete-account.html')