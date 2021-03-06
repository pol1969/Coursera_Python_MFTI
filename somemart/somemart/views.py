#import json
#
#from django.http import HttpResponse, JsonResponse
#from django.views import View
#
#from .models import Item, Review
#
#
#class AddItemView(View):
#    """View для создания товара."""
#
#    def post(self, request):
#        # Здесь должен быть ваш код
#        return JsonResponse(data, status=201)
#
#
#class PostReviewView(View):
#    """View для создания отзыва о товаре."""
#
#    def post(self, request, item_id):
#        # Здесь должен быть ваш код
#        return JsonResponse(data, status=201)
#
#
#class GetItemView(View):
#    """View для получения информации о товаре.
#
#    Помимо основной информации выдает последние отзывы о товаре, не более 5
#    штук.
#    """
#
#    def get(self, request, item_id):
#        # Здесь должен быть ваш код
#        return JsonResponse(data, status=200)
#

import json
 
from django import forms
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.core.validators import RegexValidator 
from .models import Item, Review
 
 
class GoodForm(forms.Form):
    title = forms.CharField(max_length=64,
            validators = [
               RegexValidator(
                    regex='[\D]+',
                    message='Название не д б цифрой'
                    ),
                ]
            )
    description = forms.CharField(max_length=1024,
               validators = [
               RegexValidator(
                    regex='[\D]+',
                    message='Описание не д б цифрой'
                    ),
                ]
            
            )
    price = forms.IntegerField(min_value=1, max_value=1000000)
 
 
class ReviewForm(forms.Form):
    text = forms.CharField(max_length=1024,
        validators = [
                       RegexValidator(
                            regex='[\D]+',
                            message='Описание  не д б цифрой'
                            ),
                        ]
                    
            )
    grade = forms.IntegerField(min_value=1, max_value=10)
 
 
@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""
    def is_json(self, myjson):
        try:
            json_object = json.loads(myjson)
            print(json_object)
        except json.JSONDecodeError as e:
            print("JSONDecodeError")
            return False
        return True

    def post(self, request):

        if not self.is_json(request.body): 
            return JsonResponse(status=400, data={})
#        import pdb; pdb.set_trace()

        form = GoodForm(json.loads(request.body))
 #       import pdb; pdb.set_trace()
        if request.content_type!='application/json':
            return JsonResponse(status=400, data={})
        
        if form.is_valid():
            cd = form.cleaned_data
 #           import pdb; pdb.set_trace()

            Item.objects.create(**cd)
            d = {"id":Item.objects.count()}
            return JsonResponse(d, status=201)
        return JsonResponse(status=400, data={})
 
 
@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View для создания отзыва о товаре."""
    def is_json(self, myjson):
        try:
            json_object = json.loads(myjson)
            print(json_object)
        except json.JSONDecodeError as e:
            print("JSONDecodeError")
            return False
        return True


 
    def post(self, request, item_id):
 #       import pdb; pdb.set_trace()
        if not self.is_json(request.body): 
            return JsonResponse(status=400, data={})
#

        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return JsonResponse(status=404, data={})
#        import pdb; pdb.set_trace()
        form = ReviewForm(json.loads(request.body))
        if form.is_valid():
            cd = form.cleaned_data
            cd['item'] = item
            Review.objects.create(**cd)
            d = {"id":Review.objects.count()}
            return JsonResponse(d, status=201)
        return JsonResponse(status=400, data={})
 
 
class GetItemView(View):
    """View для получения информации о товаре.
    """
 
    def get(self, request, item_id):
        try:
            item = Item.objects.prefetch_related('review_set').get(id=item_id)
        except Item.DoesNotExist:
            return JsonResponse(status=404, data={})
        item_dict = model_to_dict(item)
        item_reviews = [model_to_dict(x) for x in item.review_set.all()]
        item_reviews = sorted(
            item_reviews, key=lambda review: review['id'], reverse=True)[:5]
        for review in item_reviews:
            review.pop('item', None)
        item_dict['reviews'] = item_reviews
        return JsonResponse(item_dict, status=200)
 
