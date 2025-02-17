from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList, SecurityQuestionForm, ResetPasswordForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')
@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html',
        {'template_data': template_data})
def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        user_form = CustomUserCreationForm()
        security_question_form = SecurityQuestionForm()
        template_data['userForm'] = user_form
        template_data['securityQuestionForm'] = security_question_form
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        security_question_form = SecurityQuestionForm(request.POST)

        if user_form.is_valid() and security_question_form.is_valid():
            user = user_form.save()
            security_question = security_question_form.save(commit = False)
            security_question.user = user
            security_question.save()
            return redirect('accounts.login')
        else:
            template_data['userForm'] = user_form
            template_data['securityQuestionForm'] = security_question_form
            return render(request, 'accounts/signup.html',
                {'template_data': template_data})

def reset(request):
    template_data = {}
    template_data['title'] = 'Reset Password'
    if request.method == 'GET':
        form = ResetPasswordForm()
        template_data['form'] = form
        return render(request, 'accounts/reset.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = ResetPasswordForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/reset.html',
                    {'template_data': template_data})