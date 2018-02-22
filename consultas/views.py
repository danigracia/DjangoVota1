from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Respuesta, Pregunta, Voto


class IndexView(generic.ListView):
    template_name = 'consultas/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Pregunta.objects.order_by('-fecha_ini')[:5]


class DetailView(generic.DetailView):
    model = Pregunta
    template_name = 'consultas/detail.html'


class ResultsView(generic.DetailView):
    model = Pregunta
    template_name = 'consultas/results.html'



def vote(request, question_id):
    pregunta = get_object_or_404(Pregunta, pk=question_id)
    try:
        respuesta_sel = pregunta.respuesta_set.get(pk=request.POST['choice'])
    except (KeyError, Respuesta.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'consultas/detail.html', {
            'pregunta': pregunta,
            'error_message': "You didn't select a choice.",
        })
    else:
        respuesta_sel.num_votos += 1
        respuesta_sel.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('consultas:results', args=(question_id,)))