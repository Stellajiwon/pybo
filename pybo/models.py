from django.db import models

# Create your models here.
# 질문 모델 추가
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date=models.DateTimeField()

    # 함수 추가
    # __str__(self) 함수의 역할은
    # => 해당 클래스로 만들어진 인스턴스 자체를 출력할 때
    # 관리자 페이지에서 문자열로(제목 한글)로 출력해주는 함수이다.
    def __str__(self):
        return self.subject

# 답변 모델 추가
class Answer(models.Model) :
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
