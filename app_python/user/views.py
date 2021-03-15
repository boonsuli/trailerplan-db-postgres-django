from django.http import HttpResponse
from rest_framework import viewsets, permissions
from django.shortcuts import render, get_object_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
import logging


def index(request):
    template = loader.get_template('user/index.html')
    return HttpResponse(template.render(request=request))


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, user_id):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=user_id)
        except user.DoesNotExist:
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        idpk = int(user_id)
        user_obj = User.objects.get(pk=idpk)
        context = {
            'user': user_obj
        }
        return render(request, 'user/detail.html', context)
    elif request.method == 'PUT':
        try:
            user = User.objects.get(pk=user_id)
        except user.DoesNotExist:
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        idpk = int(user_id)
        user_obj = User.objects.get(pk=idpk)
        User.objects.update(user_obj)
        context = {
            'user': user_obj
        }
        return render(request, 'user/detail.html', context)


@api_view(['GET', 'POST', 'DELETE'])
def list(request):
    if request.method == 'GET':
        logging.debug('methode dans get')
        users = User.objects.order_by('id')
        context = {
            'users': users
        }
        return render(request, 'user/lister-parent.html', context)
    elif request.method == 'POST':
        user_form = request.data
        try:
            user = User.objects.get(pk=user_form.id)
        except user.DoesNotExist:
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        idpk = int(user_form.id)
        user_obj = User.objects.get(pk=idpk)
        User.objects.update(user_obj)
        context = {
            'user': user_obj
        }
        return render(request, 'user/lister-parent.html', context)
