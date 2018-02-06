# Photo 모델로 데이터 넣기


### (1) Admin에서 Photo 모델에 데이터 넣기

Photo 모델을 이용하여 데이터베이스를 넣겠습니다. 

View에 관련 기능을 구현해도 되지만, Django의 장점 중 하나인 Admin 기능을 이용해서 자료를 관리해 보겠습니다. 
<pre><code>from django.contrib import admin
from .models import Photo
</code></pre>

admin.site.register(Photo)
Django framework에는 Admin 기능이 admin이라는 앱 형태로 제공되는데, contrib 패키지 안에 admin 패키지로 존재합니다.

로그인을 했다면 PHOTOS라는 영역이 있고 그 아래에 Photos라는 항목이 보입니다. 그 항목이 바로 Photo 모델입니다. Photo 항목 오른쪽에 Add를 눌러보세요. Photo 모델에 데이터를 넣는 Form이 나타납니다.

본문이 채워져 있는지를 검사하고 본문에 500자 이상 입력이 안 되게 제한됩니다.

Django의 forms 기능(패키지)이 이런 처리를 하며, 이미지 파일이어야 하고 본문은 반드시 내용이 있어야 한다거나 본문 길이와 같은 검사 항목과 정보를 우리가 만든 Photo 모델에서 참조합니다.

생성일시인 created_at은 자동으로 값이 저장되는 옵션을 주어서 입력란으로 등장하지 않았습니다.


* blank 필드 옵션은 이름 그대로 빈칸을 뜻합니다. 즉 blank=True는 빈칸을 허용하겠다는 뜻입니다. 

* 이와 비슷한 옵션으로 null이 있는데, null은 Python의 None 자료형 객체를 뜻합니다. null=True는 None 자료형을 허용하겠다는 뜻입니다. 

빈칸과 None(null)은 의미가 완전히 다른데, 빈칸은 내용이 비어있는 문자형 객체입니다. 데이터베이스의 테이블 구성(schema)도 전혀 달라서, null=True이라고 하면 해당 컬럼(column)은 NULL을 허용하도록 지정되고, blank=True만 있으면 null=True가 없어서 기본값인 null=False로 지정되어 데이터베이스 테이블의 컬럼도 NULL이 허용되지 않는 NOT NULL로 지정됩니다. 

그래서 content에 blank=True 옵션만 설정한 상태에서 빈칸인 문자형 객체 조차 넣지 않으면 데이터베이스에 자료를 넣는 중에 오류가 발생합니다. 


정리하면 null=True는 데이터베이스 테이블에 대한 것, blank=True는 Django Form에 대한 설정입니다.



자, Admin 영역에서 이제 실제로 이미지 파일을 지정하여 Photo 모델에 데이터를 실제로 넣어 보세요.

### (2) 파일 업로드 경로 지정

Photo 모델에 데이터를 추가하면 업로드한 이미지 파일은 manage.py 파일이 있는 곳에 저장됩니다.

관리하기 편하게 업로드 되는 파일을 uploads/연도/월/일/종류에 저장하겠습니다.
<pre><code>image = models.ImageField(upload_to='uploads/%Y/%m/%d/orig')
filtered_image = models.ImageField(upload_to='uploads/%Y/%m/%d/filtered')
</code></pre>

위와 같이 Photo 모델을 고쳐서 저장한 후 Admin 영역에서 Photo 모델에 데이터를 추가해 보세요.
그리고 파일이 저장된 경로를 확인해 보세요. 파일이 upload_to로 지정한 경로에 저장됩니다.

경로에 저장하는 연도, 월, 일이 포함되는 것도 확인하셨나요? %Y, %m, %d가 그런 역할을 하는데, 이 문자열은 Python의 strftime의 포맷팅(formatting)에 사용되는 형태잡기 문자열(format string) 중에서 날짜와 시간과 같은 규칙을 따릅니다.


### (3) 첨부 파일 삭제하기

Admin 영역에서는 모델 객체를 추가하는 것 뿐만 아니라 기존 모델 객체를 수정하거나 지우는 기능을 기본 제공합니다. 


Django의 모델 기능은 모델 객체가 삭제되어도 그 모델 객체의 파일 필드에 연결된 파일을 지우지 않습니다. 그래서 삭제할 모델 객체를 먼져 가져와서 연결된 파일을 일일이 지워준 후에 모델 객체를 지워야 합니다.

모델 객체가 삭제될 때 그 모델 객체에 연결된 파일도 자동으로 함께 지우는 기능은 따로 구현해야 합니다. 몇 가지 방법이 있습니다.

* 모델을 삭제하는 기능이 호출되면 파일 삭제 기능도 실행

* 모델이 삭제되는 신호가 감지되면 파일 삭제 기능도 실행


Django framework은 delete라는 인스턴스 메서드를 호출하여 모델 객체를 지웁니다. 

* Admin 영역에 있는 삭제 기능도 이 메서드를 호출하는 겁니다. 이 메서드는 Model 클래스에 정의되어 있습니다. 우리가 Django 모델을 만들 때 클래스에 models.Model을 상속받도록 지정했기 때문에 우리가 만든 모델에 delete 메서드를 따로 만들지 않아도 됐던 것이지요. 


<pre><code>class Photo(models.Model):
    # 중략
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)</code></pre>

* 먼저 def delete(self, *args, **kwargs):는 특별한 내용은 없습니다.


* self.image.delete()에서 self.image는 image 모델 필드를 뜻합니다. Python 클래스의 인스턴스 메서드 안에서 속성(attribute)에 접근하려면 self.속성이름으로 접근하지요.


* 맨 마지막 줄인 super(Photo, self).delete(*args, **kwargs)는 Photo 모델이 상속받은 부모 클래스의 delete 인스턴스 메서드를 호출합니다. 넘겨받은 인자를 그대로 전달하려고 *args, **kwargs로 인자를 보내지요. 

## 부록


### Django Admin 주소


Django에서 제공하는 Admin 기능은 settings.py에 설정되어 있습니다. INSTALLED_APPS라는 변수를 찾아 보시면 django.contrib.admin이라는 줄이 보입니다. 


### Django Admin 필요성

Django Admin은 이용자가 꽤 유연하게 변경하도록 만들어져 있습니다. 서비스는 고객이 사용하는 제품부 뿐만 아니라 운영에 필요한 관리 영역을 만드는 데에도 상당한 노고가 필요한데, Django Admin을 쓰면 그런 노고가 줄어 듭니다. Django Admin은 그 자체만으로도 확장성 있게 잘 만들어져 있고, Django의 모델이나 미들웨어 체계와 강하게 연계되어 있어서 직접 구현하려면 번거로운 기능을 쉽고 편하게 구현하도록 합니다.