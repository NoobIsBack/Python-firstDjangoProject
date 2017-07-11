from django.shortcuts import render
from .models import PostModel

# Create your views here.




def post_model_detail_view(request):
	context={

	}	
	template="polls/detail-view.html"
	return render(request,template,context)


def post_model_list_view(request):
	qs=PostModel.objects.all()
	template="polls/list-view.html"
	context={
	"object_list":qs
	}

	return render(request,template,context)
