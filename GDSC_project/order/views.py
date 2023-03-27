from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Order
from django.contrib.auth.decorators import login_required
from taggit.models import Tag

def home(request):
    context  = {
        'orders': Order.objects.all(),
        'tags': Tag.objects.all()
        }
    return render(request, 'order/home.html', context)

@login_required
def favourites(request):
    fav = Order.objects.filter(favourites = request.user)
    return render(request,'order/order_favourite.html',{'fav': fav})

def order_list(request, tag_slug=None):
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug = tag_slug)
        order = Order.objects.filter(tags_in=[tag])
        return render(request, 'order/order_favourite.html', {'fav':order})
        


class PostListView(ListView):
    model = Order
    template_name = "order/home.html"
    context_object_name = "orders"
    ordering = ['time_posted']
    
    
class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Order
    
    def test_func(self):
        order = self.get_object()
        if self.request.user == order.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['order', 'customer_name', 'order_no', 'tags']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    fields = ['order', 'customer_name', 'order_no', 'tags']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        order = self.get_object()
        if self.request.user == order.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    success_url = '/'
    
    def test_func(self):
        order = self.get_object()
        if self.request.user == order.author:
            return True
        return False

@login_required
def favourite_add(request,id):
    order=get_object_or_404(Order,id=id)
    if order.favourites.filter(id=request.user.id).exists():
        order.favourites.remove(request.user)
    else:
        order.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def order_search(request):
    if request.method=='GET':
        tag = request.GET.get('search')
        if tag:
            order = Order.objects.filter(tags__name__icontains=tag)
            return render(request, 'order/order_search.html', {'fav':order})
        else:
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        