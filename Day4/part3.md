# Django Project와 App

### (1) 개념

Python 코드가 담긴 파일을 Python 모듈이라고 하며, Python package는 Python module을 묶어놓은 단위입니다.

Python 패키지는 반드시 초기화 모듈인 __init__.py이 필요합니다.

Django는 Django project 단위로 만드는데, Python 체계로 보면 Python 패키지를 뜻합니다. Django로 만드는 프로젝트에 사용되는 코드와 Django 설정값이 Python 모듈로 존재하고 모두를 포함하는 Python 패키지로 묶은 것이지요.

* 우리가 Pystagram 프로젝트를 Django로 만든다는 건 Pystagram이라는 Python 패키지를 만들고
 
* Pystagram에 들어가는 기능은 Python 모듈로 만든다는 뜻입니다.

* 이 디렉터리는 Python 패키지니까 초기화 파일인 __init__.py이 필요합니다.
 
* 그리고 Django framework이 참조할 프로젝트 설정 항목은 settings라는 모듈이므로 settings.py라는 파일로 필요합니다.

*  웹 주소(URL)로 서비스에 접근하므로 각 접근 주소에 연결될 기능을 설정하는 urls.py라는 파일도 필요합니다. 

### (2) Django project 만들기

Python 패키지인 Pystagram 디렉터리를 만들고, 
여기에 필수 모듈인 settings.py와 __init__.py를 만드는 과정을 간편하게 처리하는 프로그램이 django-admin.py입니다. 

<code> source env_pystagram/bin/activate</code>

<code>django-admin startproject pystagram</code>


Django Project와 Python 패키지

앞으로 만들 Pystagram 소스 파일이나 각종 매체(media) 파일은 이곳에 담는데,
이 디렉터리 자체는 Python 패키지는 아닙니다. Python 패키지가 아니므로 Python으로 불러들일 수 없고(import)
그러므로 이 디렉터리 이름은 Pystagram으로 하든 HelloWorld로 하든 아무 상관 없습니다.


pystagram 디렉터리 안에 있는 pystagram 디렉터리가 실제로 사용되는 Python 패키지입니다.
이 디렉터리는 Pystagram 프로젝트에서 사용할 시작 패키지라고 보면 됩니다.


### (3) Pystagram Project 초기/사전 작업

django-admin.py로 Pystagram project를 만들고 나면 데이터베이스를 동기화하는 과정을 거칩니다.
데이터베이스를 전혀 사용하지 않는다면 생략하기도 합니다. 데이터 자체는 외부에서 매번 요청하여 가져오고,
이 데이터를 적절히 가공하여 바로 출력하면 굳이 데이터베이스를 쓰지 않아도 됩니다. 

하지만 Pystagram은 데이터베이스를 사용합니다.

<code>python manage.py migrate</code>

manage.py에 migrate 명령어를 주면 Django framework에서 제공하는 도구가 사용하는 데이터베이스 관련 작업을 자동으로 진행합니다. 

<code>python manage.py createsuperuser</code>

<code> python manage.py changepassword hannal</code>

이렇게 수행한 데이터베이스 작업은 db.sqlite3라는 파일에 저장됩니다.

Python도 sqlite의 데이터베이스를 다루는 API를 기본 내장하고 있습니다.

### (4) Photo App 초기 작업

Django App

가장 먼저 기획한 기능은 사진 관련 기능이었습니다. 그 다음이 사용자와 회원 기능, 그 다음이 사진 모아보는 기능이었지요. 이 각각은 사진 올리기, 사진 보기와 같이 세부 기능이 묶여 있지요. 

이렇게 목적을 가진 뭔가를 수행하는 애플리케이션(application)을 Django계에선 Django App이라고 부릅니다.

보통은 Django App은 해당 App으로 분리된 Python 패키지 형식입니다. 

<code>python manage.py startapp photos</code>

* admin.py는 관리자 영역에서 이 App을 다루는 코드를 담는 모듈입니다. 
* models.py은 모델을 정의하는 모듈인데 모델(model)은 데이터(data)를 구성하는 항목 자체(field)와 데이터를 다루는 행위(behaviour)를 포함한 것입니다. 

* views.py는 특정 주소(URL)에 접근하면 화면에 내용을 표시하는 Python 함수를 호출하는 내용을 담습니다

(MVC 패턴에서는 View가 표현물이지만, Django계에서는 template이 표현물입니다. Django에서 View는 데이터(모델)를 표현(템플릿)하는 연결자이자 안내자입니다. MVC 패턴으로 보면 Controller와 유사합니다.)

* tests.py은 Unit test 내용을 담는 모듈입니다.


### (4) Photo App 만들기

Photo model 만들기

Django project에서 모델은 db package의 models 모듈에 있는 Model 클래스(class) 사용하여 만듭니다. 

그럼 Model 클래스를 사용하여 photos App에 Photo 모델을 만들어 보겠습니다. 이 모델은 사진을 다루는 기본 데이터를 다룹니다. 모델이니 models.py를 고쳐야겠지요?



<pre><code>from django.db import models

class Photo(models.Model):
    id = '개별 사진을 구분하는 색인값'
    image = '원본 사진 파일'
    filtered_image = '필터 적용된 사진 파일'
    content = '사진에 대한 설명문'
    created_at = '생성일시'</code></pre>
    

Django에서 모델의 속성(attribute)은 데이터베이스 필드(field)로 나타냅니다. 

Python 클래스로 놓고 보면 속성이지만, Django 모델의 데이터 요소로 다루고자 할 경우 Django 모델이 제공하는 별도 자료형(type)으로 값을 다루는데, 이 자료형인 값을 모델 필드라고 하지요. 그래서 위 모델에서 image, content 등은 아직은 그냥 Python 클래스 속성입니다.


이제 이 속성들을 Django 모델 필드로 바꾸겠습니다.

* 모델 필드에는 몇 가지 선택 항목을 지정

* filtered_image는 원본 이미지 파일에 필터(filter)를 적용한, 즉 가공을 거친 파일입니다. 
* content는 사진에 사진글 작성자가 기입한 내용입니다. 그냥 글자만 넣으면 되는데, 글자를 입력하는 필드 타입은 CharField와 TextField가 있습니다.

* 문자열을 다룬다는 점에서 CharField와 TextField는 같지만, 실은 전혀 다릅니다. CharField는 데이터베이스의 VARCHAR에 대응합니다. Django는 통상 250자 정도를 보장합니다. 

* created_at은 Photo 모델이 생성되어 데이터베이스에 저장되는 시각을 담는데, Django에는 날짜를 다루는 DateField, 시간을 다루는 TimeField, 그리고 날짜와 시간을 같이 다루는 DateTimeField가 있습니다. 생성일시 정보를 다루니 DateTimeField를 쓰겠습니다. 

<pre><code>from datetime import datetime

the_photo.save()

if the_photo.is_created is True:
    the_photo.created_at = datetime.now()
    the_photo.save()
</code></pre>

최초 생성 일시 : auto_now_add=True, auto_now_add=False
매 변경 일시 : auto_now_add=True, auto_now=True

Django 1.8판부터는 다음과 같이 사용합니다.

최초 생성 일시 : auto_now_add=True
매 변경 일시 : auto_now=True


자, 이제 그냥 클래스 속성으로 구성된 기존 Photo 모델을 Django 모델로 바꿔 보겠습니다. 

<pre><code>class Photo(models.Model):
    image = models.ImageField()
    filtered_image = models.ImageField()
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)</code></pre>
데이터베이스에 반영 (migration)


설치를 마치면 다시 마이그레이션 스크립트를 만듭니다.

<code>python manage.py makemigrations</code>


<code>python manage.py migrate</code>

이렇게 해서 Photo 모델을 데이터베이스에 반영하여 연결하였습니다. 


## 부록

### MTV와 MVC

Django는 Model, Template, View의 앞자를 따서 MTV 패턴을 따릅니다. Model-View-Controller인 MVC 패턴과 유사한데, 실제로 많은 사람은 이 패턴의 개념에 별 차이를 두지 않습니다. Django의 View는 MVC 패턴의 Controller, Template은 MVC 패턴의 View로 적당히 퉁쳐서 이해합니다. 역할로 보면 그다지 틀린 말도 아니지만, Django framework가 지향하는 철학면에서 보면 MTV 패턴과 MVC 패턴엔 미묘한 차이가 있습니다.

재료를 가공하여 손에 닿는 결과물로 만드는 상황을 가정하지요. 여기서 재료란 Data, 즉 Model이고, 재료로 만들어 낸 결과물이 View입니다. 가공하는 행위자가 바로 Controller지요. 이게 MVC 패턴이라면, Django 소프트웨어 재단에서는 MVC 패턴의 Controller 역할은 Django framework 그 자체가 하고 있다고 봅니다.

