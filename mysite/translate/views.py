from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.http import urlencode
from googletrans import Translator, LANGCODES



# Create your views here.
# def index(request):
#   return HttpResponse("Hello, world. You're at the translate index.")

class IndexView(generic.TemplateView):
  template_name = 'translate/index.html'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['lang_list'] = LANGCODES
    if 'input_text' in self.request.GET:
      context['input_text'] = self.request.GET['input_text']
    if 'translation' in self.request.GET:
      context['translation'] = self.request.GET['translation']
    if 'dest_lang' in self.request.GET:
      context['dest_lang'] = self.request.GET['dest_lang']
    return context

def translate(request):
  text_to_translate = request.GET['input_text']
  destination_language = request.GET['dest_lang']
  translator = Translator()
  translation = translator.translate(text=text_to_translate, dest=destination_language, src='auto')
  redirect_url = reverse("translate:index")
  parameters = urlencode({'input_text': text_to_translate, 'translation': translation.text, 'dest_lang': destination_language}) 
  return HttpResponseRedirect(f'{redirect_url}?{parameters}')
  pass

def clear(request):
  return HttpResponseRedirect(reverse("translate:index"))