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

## mysql 사용시
```shell script
# mysql 설치
pip install mysqlclient
``` 
```python
# settings.py 파일에 추가
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '데이터베이스 이름',
        'USER': '사용자이름',
        'PASSWORD': '패스워드',
        'HOST': 'RDS엔드포인트 URL 복사',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"

        }

    }
}
```
```shell script
# 장고 DB모델 초기화
python manage.py migrate
``` 

# 1. 클라이언트(order) 기본
- `template`: html 등 화면 관련된 폴더

# 2. 관리자(boss) 기본
## 프로젝트 생성
`python manage.py createsuperuser`



# 3. 배달기사(delivery) 기본
## 프로젝트 생성 및 루트연결
```
# 1. app 생성
python manage.py startapp delivery
# 2. root프로젝트(mysite) -> urls.py 파일에 입력
path('delivery/', include('delivery.urls')),
# 3. root프로젝트(mysite) -> settings 파일에 입력
INSTALLED_APPS = ['delivery'] 
``` 
## 프로젝트 세팅
1. urls.py 생성
2. views.py 생성
3. templates 폴더 생성 -> html파일 생성


# 기타 - Rest framework 사용
- https://www.django-rest-framework.org/tutorial/quickstart
- 위 url로 접속하여 기본 튜토리얼 따라해보기