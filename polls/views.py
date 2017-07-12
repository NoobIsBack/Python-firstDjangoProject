from django.shortcuts import render
from .models import PostModel
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.




def post_model_detail_view(request,id=None):
  
	# import ipdb;ipdb.set_trace() 


  	try:
		detail_object=PostModel.objects.get(id=id)
  	except:
  		raise Http404
  	context={
    	 "detail_obj":detail_object
  	}	
  	template="polls/detail_view.html"
	return render(request,template,context)



@login_required
def post_model_list_view(request):

	print request.user
	qs=PostModel.objects.all()
	template="polls/list_view.html"
	context={
	"object_list":qs
	}

	return render(request,template,context)
