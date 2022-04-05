# 프로젝트 시작
python manage.py runserver

# 앱 생성 및 구동
python manage.py startapp polls

# 데이터베이스 마이그레이션
python manage.py migrate

# 데이터베이스 App을 마이그레이션
python manage.py makemigrations polls

# 데이터베이스 Shell 접속
python manage.py shell

# 종료
exit()

```shell
# 데이터 insert 
from polls.models import Choice, Question
Question.objects.all()
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
q.question_text
q.pub_date
```