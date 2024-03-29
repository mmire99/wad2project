from django.shortcuts import render,get_object_or_404
from .models import Thread,Category,Reply
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .forms import ThreadForm,ReplyForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound


def Categories(request,category):
	category_objects = Thread.objects.filter(category=category).order_by('-id')
	if not category_objects:
		return HttpResponseNotFound('<h1>Page not found</h1>')
	else:
		category_objects = Thread.objects.filter(category=category).order_by('-id')
		return render(request,'stormwind/categories.html',{'cats':category,
										     'category_objects':category_objects})


@login_required
def profile(request):
	user = request.user
	threads = Thread.objects.filter(member=request.user).order_by('-date_created')
	paginator = Paginator(threads,4)
	page_obj = paginator.page(request.GET.get('page',1))
	t_count = threads.count()

	return render(request,'users/profile.html',{'page_obj':page_obj,
												'user': user,
												't_count':t_count})

def likeButton(request,pk):
	t = get_object_or_404(Thread,id=request.POST.get('thread_id'))
	liked = False
	if not t.likes.filter(id=request.user.id).exists():
		t.likes.add(request.user)
		liked = True
	else:
		t.likes.remove(request.user)
		t = False
	return HttpResponseRedirect(reverse('detail-view',args=[str(pk)]))



class Home(ListView):
	model = Thread
	template_name = 'stormwind/home.html'
	ordering = ['-date_created']

	def get_context_data(self,*args,**kwargs):
		cats = Category.objects.all()
		latest_threads = Thread.objects.all().order_by('-id')[:4]
		threads = Thread.objects.all()
		gameplay_homepage = Thread.objects.filter(category="GamePlay").order_by("-id")[:5]
		community_homepage = Thread.objects.filter(category="Community").order_by("-id")[:5]
		classes_homepage = Thread.objects.filter(category="Classes").order_by("-id")[:5]
		guides_homepage = Thread.objects.filter(category="Guides").order_by("-id")[:5]
		context = super(Home,self).get_context_data(*args,**kwargs)
		context['cats'] = cats
		context['latest_threads'] = latest_threads
		context['threads'] = threads
		context['gameplay_homepage'] = gameplay_homepage
		context['community_homepage'] = community_homepage
		context['classes_homepage'] = classes_homepage
		context['guides_homepage'] = guides_homepage
		return context


class ThreadDetailView(DetailView):
	model = Thread
	template_name = 'stormwind/thread_detail.html'

	def get_context_data(self,*args,**kwargs):
		cat_menu = Category.objects.all()
		context = super(ThreadDetailView,self).get_context_data(*args,**kwargs)
		context['liked'] = get_object_or_404(Thread,id=self.kwargs['pk']).likes.filter(id=self.request.user.id).exists()
		context['cat_menu'] = cat_menu
		context['total_likes'] = get_object_or_404(Thread,id=self.kwargs['pk']).total_likes()
		return context

class AddThreadView(CreateView):
	model = Thread
	form_class = ThreadForm
	template_name = 'stormwind/create_thread.html'
	def form_valid(self,form):
		form.instance.member = self.request.user
		return super().form_valid(form)

class DeleteThread(DeleteView):
	model = Thread
	template_name = 'stormwind/delete_thread.html'
	success_url = reverse_lazy('home')

class ReplyToThread(CreateView):
	model = Reply
	form_class = ReplyForm
	template_name = 'stormwind/reply.html'

	def form_valid(self,form):
		form.instance.name = self.request.user
		form.instance.img_url = self.request.user.profile.profile_pic
		form.instance.thread_id = self.kwargs['pk']
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('detail-view', kwargs={'pk': self.kwargs['pk']})

class UpdateThread(UpdateView):
	model = Thread
	# form_class = UpdateForm
	template_name = 'stormwind/updateThread.html'
	fields = ['title','content']
