from django.shortcuts import render, get_object_or_404, redirect
# 추가
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm
# Create your views here.

# HttpResponse 클래스는 페이지 요청에 대한 응답을 할 때 사용하는 장고 클ㄹ래스이다.
def index(request):
    """
    pybo 목록 출력
    """
    # '-create_date'는 질문의 작성일시가 최근에 작성한 순으로 내림차순하겠다는 의미
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'pybo/question_list.html', context)

    #return HttpResponse("안녕하세요 pybo App에 오신것을 환영합니다.")
def detail(request, question_id) :

    """
    pybo 내용 출력
    """

    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    답변 등록 처리 함수 구현
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # 답변 등록 후 상세 화면으로 이동
    return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    """
    pybo 질문생성
    """
    #클라이언트에서 서버에 요청 시 GET 방식인지 POST 방식으로 전달할건지 따라 처리
    if request.method == 'POST': #POST 방식
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else: # GET 방식
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
