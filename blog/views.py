from blog.models import Blog
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    ontext_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"


class BlogCreateView(CreateView):
    model = Blog
    template_name = "blog/blog_form.html"
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blog/blog_form.html"
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
