from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from todo.models import Tasks


def index(request):
    # return HttpResponse('Hello World! This is the first response')
    return HttpResponse('<H1>Hello world</H1>')


def index(request):
    # return HttpResponse('Hello World! This is the first response')
    return render(request, 'index.html', context={}, status=200)


class TasksView(GenericAPIView):
    http_method_names = ('get', 'post', 'create', 'delete')

    def get(self, request, **kwargs):
        print('TasksView - get')
        # result = list(Tasks.objects.exclude(action='archived').values())
        result = list(Tasks.objects.values())
        return JsonResponse(result, safe=False)

    def post(self, request, **kwargs):
        print('TasksView - post')
        post_data = request.data
        if post_data.get('action') == 'archive':
            selected_ids = post_data.get('selected_ids')
            Tasks.objects.filter(id__in=selected_ids).update(
                action='archived'
            )
        elif post_data.get('action') == 'delete':
            selected_ids = post_data.get('selected_ids')
            Tasks.objects.filter(id__in=selected_ids).delete()
        else:
            Tasks.objects.filter(id=post_data.pop('id')).update(**post_data)
        return JsonResponse({'status': 'success'}, safe=False)

    def create(self, request, **kwargs):
        print('TasksView - create')
        request_data = request.data
        Tasks(
            title=request.data['title'],
            description=request.data['description'],
            action='created',
            target_date=request.data['target_date']
        ).save()
        return JsonResponse({'status': 'success'}, safe=False)

    def delete(self, request, **kwargs):
        print('TasksView - delete')
        delete_data = request.data
        Tasks.objects.filter(id=delete_data.pop('id')).delete()
        return JsonResponse({'status': 'success'}, safe=False)
