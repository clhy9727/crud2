import json

# from django.shortcuts import render
from django.http    import JsonResponse
from django.views   import View

from owners.models import Owner, Dog

# Create your views here.
class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )

        return JsonResponse({'message':'created'}, status=201)

    
    def get(self, request):
        owners = Owner.objects.all()
        results = []

        for owner in owners:
            results.append(
                {
                    "name" : owner.name,
                    "email" : owner.email,
                    "age" : owner.age
                }
            )

        return JsonResponse({'reults':results}, status=200)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(name=data['owner'])
        dog = Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner = owner
        )

        return JsonResponse({'message':'created'}, status=201)


    def get(self, request):
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:
            results.append(
                {
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" : dog.owner.name
                }
            )

        return JsonResponse({'reults':results}, status=200)