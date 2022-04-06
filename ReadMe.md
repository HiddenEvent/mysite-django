# 장고 기본 생성
## 프로젝트 시작
python manage.py runserver

## 앱 생성 및 구동
python manage.py startapp polls

## 데이터베이스 마이그레이션
python manage.py migrate

## 데이터베이스 App을 마이그레이션
python manage.py makemigrations polls

## 데이터베이스 Shell 접속
python manage.py shell

## 종료
exit()
## sqllite DB 제어 사용방법
```shell
# 데이터 insert 
from polls.models import Choice, Question
Question.objects.all()
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()

# select
q.id
q.question_text
q.pub_date
q = Question.objects.get(pk=1)
q.was_published_recently()
```

# 관리자 기본
## 프로젝트 생성
`python manage.py createsuperuser`


