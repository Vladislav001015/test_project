from applications.music.models import Music
from applications.music.serializers import MusicSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404



@api_view(['GET'])
def get_music(request):
    """retrive all task object"""
    tasks = Music.objects.all()
    serializer = MusicSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def misic_detail(request, id):
    try:
        task = Music.objects.get(id=id)
        serializer = MusicSerializer(task, many=False)
    except Music.DoesNotExist:
        raise Http404
    return Response(serializer.data)


from rest_framework import status


@api_view(['POST'])
def task_create(request):
    print('===================')()
    # print(dir(request))
    print('===================')
    # print(request.data)
    print('===================')
    serializer = MusicSerializer(data=request.data) # нужно это преобразовать в понятный питону формат
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH']) # update
def task_edit(request, id):
    try:
        task = Music.objects.get(id=id)
        if request.method == 'PUT':
            serializer = MusicSerializer(instance=task, data=request.data)
        elif request.method == 'PATCH':
            serializer = MusicSerializer(instance=task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Music.DoesNotExist:
        raise Http404


@api_view(['DELETE'])
def task_delete(request, pk):
    try:
        task = Music.objects.get(id=pk)
        task.delete()
        return Response("Task deleted successfully", status=status.HTTP_204_NO_CONTENT)
    except Music.DoesNotExist:
        raise Http404

@api_view(['GET'])
def api_overview_links(request):
    urls = {
        'lists_todo': 'musics/',
        'detail_todo': 'music-detail/<int:id>',
        'create_todo': 'task-create/',
        'edit_todo': 'task-edit/<int:id>/',
        'delete_todo': 'task-delete/<int:pk>/'
    }
    for i in urls:
        urls[i] = request.build_absolute_uri() + urls[i]
    return Response(urls)



# ORM django основан на querySet
# querySet – это набор обьектов из БД который может использоваться для ограничения результатов(т.е SELECT – то
# queryset, a filters это условие или же лимит – WHERE)
# querySet – по сути список обьектов заданной модели, он позволяет читать данные из БД фильтровать и изменять их
# порядок и тд
# Мы получаем queryset используя manager и по умолчанию он называется objects, обратится к нему можно через класс
# модели



# представление - определяет функции : чтение. Создание обновдление удаление

# 	Есть :
# 	    Function-based view(FBV) – нужно обернуть функицю представление в декоратор api_view([‘GET’]) – в скобках
# 	указывая какими методами отпралять view и так же необходимо указать сериализатор который будет приводит в нужный
# 	формат

# 		Class-based view(CBV) - (с версии 1.3) - способ описание view в виде классов
# 		1 способ неаписат ькласс от (ApiView) импортируется от rest_frame_work_views
#       2 способ – написание классов от generics views котрый импортируется из библиотеки рест фреймворк есть много
# различных видов(ListApiView,CreateApiView,RetrieveApiView,UpdateApiView,DestroyApiView и тд) и так же необходимо
# указывать сериализатор

# CRUD (Джейсон Мартин) -стандартная классификация функций по манипуляции данными
# С (insert) post, R(Select) get, U(Undate) D(Delete) delete
# Можно реализовать 2-мя способами:
# 1) Реализация на (function based view) – представление основанное на функции
# 2) на class based view (с версии 1.3)- способ описание view в виде классов
# listview – список обьектов
# detailview - детализация
# CreateView
# UpdateView
# DeleteView
# атрибут form_class – является обязательным для создания или же  обновления обьекта


from rest_framework import generics


class MovieListView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MovieCreateView(generics.CreateAPIView):
    serializer_class = MusicSerializer


class MovieDeleteView(generics.DestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MovieDetailView(generics.RetrieveAPIView):
    lookup_field = 'title'
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MovieUpdateView(generics.UpdateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class CommentListCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

# ListCreateAPIView