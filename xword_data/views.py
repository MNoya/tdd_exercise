from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View

from . import models


class DrillView(View):
    template_name = 'drill.html'

    def get(self, request, *args, **kwargs):
        random_clue = models.Clue.get_random_clue()
        return render(request, self.template_name, context=self._get_context_for_clue(random_clue))

    def post(self, request, *args, **kwargs):
        data = request.POST
        clue_id = data.get('clue_id')
        clue = models.Clue.objects.get(id=clue_id)
        if data.get('answer').lower() == clue.entry.entry_text.lower():
            return redirect(reverse('xword-answer', kwargs={"clue_id": clue.id}))
        else:
            messages.error(request, "Answer is not correct")
            # TODO: Save correct/incorret answers in session
            return render(request, self.template_name, self._get_context_for_clue(clue))

    @staticmethod
    def _get_context_for_clue(clue):
        return {
            'clue_id': clue.id,
            'clue_text': clue.clue_text,
            'puzzle': clue.puzzle,
        }


def answer(request, clue_id):
    return render(request, 'answer.html', {})
