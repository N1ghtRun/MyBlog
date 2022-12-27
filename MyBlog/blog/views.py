from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator

from .models import Post, Category


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ['-pub_date']
    paginate_by = 5


class CategoryView(DetailView):
    model = Category
    template_name = "blog/category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(category=self.object)

        # Paginator
        paginator = Paginator(posts, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj

        return context


class SinglePostView(DetailView):
    model = Post
