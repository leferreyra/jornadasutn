from website.models import Jornada
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):

	jornada = Jornada.objects.all().order_by("-id")[0]

	return render_to_response('index.html', {'jornada': jornada},
			context_instance=RequestContext(request))	
