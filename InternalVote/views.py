from django.shortcuts import render
from django.http import HttpResponse

# ====================================================

from .models import Award, AwardMst
from .forms import AwardForm

# ====================================================

def index(request):
    """ Index
    """
    awd_mst = AwardMst.objects.order_by('id')
    if request.method == "POST":
        form = AwardForm(request.POST)
        print('####  DEBUG #####')
        print(form)
        print('##### DEBUG #####')
        if form.is_valid():
            # save
            post = form.save(commit=False)
            print('####  DEBUG #####')
            post.save()
            print(post)
            print('####  DEBUG #####')
            # new form
            form = AwardForm()
            context = {
                'form': form,
		'awd_mst': awd_mst,
            }
            return render(request, 'InternalVote/index.html', context)
    else:
        pass

    form = AwardForm()
    print('####  DEBUG #####')
    print(form)
    print('####  DEBUG #####')
    context = {
        'form': form,
        'awd_mst': awd_mst,
    }
    return render(request, 'InternalVote/index.html', context)

# ====================================================

def result(request):
    """ Result
    """
    awd = Award.objects.order_by('create_date')
    context = {
        'awd': awd,
    }
    return render(request, 'InternalVote/result.html', context)

