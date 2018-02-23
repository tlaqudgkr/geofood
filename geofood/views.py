from django.shortcuts import render

from geofood.models import Restaurant, Category

from django.shortcuts import redirect, get_object_or_404

from geofood.forms import PostForm, RestForm
# Create your views here.

def rest_list(request):
    food = Category.objects.all()
    ctgry = request.GET.get('category')
    if ctgry != None:
        posts = Restaurant.objects.filter(category__name = ctgry)
    else:
        posts = Restaurant.objects.all()

    return render(request, 'rest/rest_list.html', {'food':food,'posts':posts})


def rest_detail(request, pk):
    rest = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'rest/rest_detail.html', {'rest':rest})


def rest_new(request):
    if request.method == 'POST':
        form = RestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('rest:rest_detail', pk=post.pk)
    else:
        form = RestForm()
        postForm = PostForm()
    return render(request, 'rest/rest_edit.html', {'form': form, 'postform': postForm})


def rest_edit(request,pk):
    post = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('rest:rest_detail', pk=post.pk)
    else:
        form = RestForm(instance=post)
        postForm =PostForm(instance=post)
    return render(request, 'rest/rest_edit.html', {'form': form, 'postform': postForm})


def rest_remove(request,pk):
    post = get_object_or_404(Restaurant, pk=pk)
    post.delete()
    return redirect('rest:rest_list')


