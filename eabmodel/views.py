from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseNotFound

from users.models import EvaluatorUser
from users.forms import EvaluatorUserCreationForm, EvaluatorUserRemoveForm

from .models import Course
from .forms import CourseForm, RemoveCourseForm


# Create your views here.

@login_required
def landingpage(request):
    context = {}
    return render(request, 'eabmodel/landingpage.html', context)


@login_required
def courses(request, extra_context={}):
    if not request.user.is_admin:
        return HttpResponseNotFound('Sorry')

    form = CourseForm()
    course_list = Course.objects.all().order_by('updated_at', 'created_at').reverse()
    context = {'course_list': course_list,
               'form': form,
               }

    context.update(extra_context)
    return render(request, 'eabmodel/course.html', context)


@login_required
def add_course(request):
    if not request.user.is_admin:
        return HttpResponseNotFound('Sorry')

    if request.method != 'POST':
        form = CourseForm()
    else:
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()

    extra_context = {'form': form, 'form_msg': True}
    response = courses(request, extra_context)
    return response


@login_required
def remove_course(request):

    if not request.user.is_admin:
        return HttpResponseNotFound('Sorry')

    if request.method == 'POST':
        form = RemoveCourseForm(request.POST)
        if form.is_valid():
            course = Course.objects.get(pk=form.cleaned_data['id'])
            course.delete()
    return redirect(reverse('main:courses'))



@login_required
def evaluators(request, extra_context={}):

    if not request.user.is_admin:
        return HttpResponseNotFound('Sorry')

    form = EvaluatorUserCreationForm()

    evaluator_list = EvaluatorUser.objects.all()\
        .filter(is_active=True)\
        .exclude(pk=request.user.id)\
        .order_by('date_joined')\
        .reverse()

    context = {'evaluator_list': evaluator_list,
               'form': form,
               }

    context.update(extra_context)
    return render(request, 'eabmodel/evaluator.html', context)


@login_required
def add_eval(request):
    if not request.user.is_admin:
        return HttpResponseNotFound('Sorry')

    if request.method != 'POST':
        form = EvaluatorUserCreationForm()

    else:
        form = EvaluatorUserCreationForm(request.POST)
        if form.is_valid():
            evaluator = form.save(commit=False)
            password = EvaluatorUser.objects.make_random_password()
            evaluator.set_password(password)
            evaluator.save()

    extra_context = {'form': form, 'form_msg': True, 'password': password}
    response = evaluators(request, extra_context)
    return response


@login_required
def remove_eval(request):

    if not request.user.is_admin:
        return HttpResponseNotFound('Sorry')

    if request.method == 'POST':
        form = EvaluatorUserRemoveForm(request.POST)
        if form.is_valid():
            evaluator = EvaluatorUser.objects.get(pk=form.cleaned_data['id'])
            evaluator.delete()
    return redirect(reverse('main:evaluators'))


