from django.shortcuts import render
from .models import Post,Category
from django.views.generic import DetailView, ListView
# Create your views here.
def index(req):

    post_list = Post.objects.all()
    
    if req.GET.get("author",False):
        author= req.GET.get("author",False)
        post_list=Post.objects.filter(author__exact=author)

    if req.GET.get("categori",False):
        category= req.GET.get("categori",False)
        post_list=Post.objects.filter(category__Category_name=category)

    return render (req,"blogapp/index.html", context={"posts": post_list} )

class PostDetailView(DetailView):
    template_name ="blogapp/post_detail.html"

    model = Post

class CatergoriList(ListView):
    template_name="blogapp/categori_list.html"

    model= Category
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categori_list"]= self.get_queryset()

        return context

class AuthorList(ListView):
    template_name="blogapp/autor_list.html"

    model= Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["author_list"]= []
        for post in self.get_queryset():
            if not post.author in context["author_list"]:
                context["author_list"].append(post.author)


        return context
