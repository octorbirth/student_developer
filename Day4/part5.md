인터넷 주소에 접속하여 Photo 모델로 올린 사진 데이터를 가져와서 View 기능을 이용하여 웹 브라우저에 관련 내용을 출력해보겠습니다.

## 1. URL에 Photo View 연결

### (1) URL Resolver


이용자가(client) 인터넷 주소(URL : Uniform resource locator, 이하 URL)로 접속하면 웹 서버는 접속한 주소에 해당하는 내용물을 보여줍니다. Django로 운용되는 서비스도 마찬가지여서, 이용자가 URL로 접근하여 뭔가를 요청하면 그 URL에 대한 정보를 urls.py로 대표되는 URL dispatch에서 찾아서 연결된 구현부를 실행합니다.

URL과 구현부을 연결해주는 역할을 Django의 View 영역인 views.py가 합니다.  
View에서 URL로 요청받은 걸 이런저런 방법으로 처리하여 결과(출력물)를 내보낸다고 보면 됩니다.

Django에서는 URL Resolver(urlresolver)라는 모듈이 URL Dispatch 역할을 하며,
urlresolvers 모듈에 있는 RegexURLResolver 클래스가 요청받은 URL을 되부를 함수(callback function) 덩어리로 바꿔줍니다. 


* BaseHandler 클래스가 URL로 요청(request) 받음
* RegexURLResolver로 URL을 보냄
* RegexURLResolver가 URL에 연결된 View를 찾아서 callback 함수와 인자 등을 BaseHandler로 반환
* BaseHandler에서 이 함수를 실행하여 결과값인 출력물을 받음.
* 출력



### (2) 개별 사진 보기 View - 1

photos 앱, 그러니까 photo 디렉터리 안에 있는 views.py 파일을 엽니다. 별 내용은 없습니다. 세상에 인사하는 View부터 구현해보겠습니다.

<pre><code>from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('안녕하세요!')</code></pre>
    

이번엔 pystagram 디렉터리에서 urls.py 파일을 열어서 주석으로 표기한 두 줄을 추가합니다.

<pre><code>from django.conf.urls import url
from django.contrib import admin

from photos.views import hello  # 이 줄을 추가하고, 

urlpatterns = [
    url(r'^hello/$', hello),  # 이 줄도 추가합니다.
    url(r'^admin/', admin.site.urls),
]</code></pre>

### (3) urls.py

urls.py에는 Django의 urls 모듈에 있는 url 함수를 이용하여 URL 연결자를 만들어서 urlpatterns에 넣습니다.

주소 연결자를 만드는 url 함수 부분을 보겠습니다. 이 함수는 총 네 개 인자를 받습니다.

* regex : 주소 패턴 (정규표현식)
* view : 연결할 View
* name : 주소 연결자 이름
* kwargs : urls에서 View로 전달할 dict형(사전형) 인자
* regex와 view는 필수 인자이고, 나머지는 생략해도 됩니다.

이번엔 개별 사진을 보는 URL을 만들겠습니다. 

<pre><code>from django.conf.urls import url
from django.contrib import admin

from photos.views import hello
from photos.views import detail  # 이 줄이 추가됐고,


urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^photos/(?P<pk>[0-9]+)/$',  # 이 줄과
        detail, name='detail'),  # 이 줄도 추가
    url(r'^admin/', admin.site.urls),
]</code></pre>


사진 게시물을 보는 URL은 `/photos/<사진 ID="">/'입니다.

사진 ID는 숫자이므로 URL은 이런 구조입니다. 주소 중 숫자 ID 부분만 다르고 나머지는 동일합니다. 
그리고 숫자 ID는 숫자로 구성되어 있습니다. 이런 문자열 패턴을 다루는 방법 중 하나가 정규표현식입니다. 

##### ^photos/(?P<pk>[0-9]+/$' 를 하나씩 파헤쳐 봅시다.

* ^ : ^ 문자 뒤에 나열된 문자열로 시작
* [0-9] : 0부터 9까지 범위에 속하는 문자
* + : 앞에 지정한 문자열 패턴이 한 번 이상 반복
* () : 패턴 부분을 묶어냄(grouping)
* ?P<pk> : 묶어낸 패턴 부분에 이름을 pk로 붙임.
* $ : $ 문자 앞에 나열된 문자열로 끝
* +을 빠뜨리지 마세요. [0-9]로만 패턴을 정하면, 숫자 ID는 한 자리 숫자만 뜻합니다.


이번엔 photos 앱 디렉터리의 views.py 파일을 열고 detail 뷰 함수를 만듭니다. 
<pre><code>def detail(request):
    return HttpResponse('detail 뷰 함수')</code></pre>

### (4) 개별 사진 보기 View - 2

웹브라우저에서 detail 함수가 이 인자를 받도록 해야 합니다.

<pre><code>def detail(request, pk):
    msg = '{}번 사진 보여줄게요.'.format(pk)
    return HttpResponse(msg)</code></pre>
    
urls.py에서 뷰 함수로 넘길 인자 이름을 지정하지 않아도 별 문제는 없습니다.

url(r'^photos/([0-9]+)$', detail, name='detail'),
urls.py에서 위와 같이 ?P<pk>을 빼서 인자 이름을 없애면, 인자는 위치 인자로(positional argument) 뷰 함수로 넘겨집니다.



## 2. Photo 모델에서 사진 정보를 가져와 출력하기

### (1) Photo 모델로 객체 찾기(lookup)

먼저 from .models import Photo문으로 photos 앱에 있는 models 모듈에서 Photo 모델을 가져옵니다. .models는 photo.models와 같은 내용인데, views.py 파일과 같은 디렉터리(경로)에 있기 때문입니다.

그 다음에 Photo 모델의 objects 객체의 get 메서드를 이용해 뷰 함수의 인자 pk에 해당하는 사진 데이터(Photo 모델의 객체(instance)) 가져와서 photo라는 변수에 담습니다.

Photo 모델에 있는 image이라는 필드에 접근해서 url 속성(property)를 이용해 지정한 사진의 URL을 출력합니다.

### (2) 찾는 객체가 없으면 404 오류 출력

/photos/숫자/ URL 중 숫자를 되게 큰 값, 예를 들어 1023을 넣어보세요. “DoesNotExist at /photos/1023/”라는 오류가 출력됩니다. 사진 ID 중 1023번인 자료가 없어서 모델 영역에서 발생한 오류입니다. 이 오류 대신 “사진이 없다”는 안내를 하려면 이 오류에 대한 예외(exception) 처리를 해야 합니다.



### (3) 업로드한 파일을 URL로 접근하기


먼저 화면에 출력된 사진 파일 URL로 이미지를 출력하도록 HTML 태그를 출력할 내용에 추가하겠습니다. img 태그를 쓰는 것이지요.

웹브라우저로 접속해보세요. 이미지가 출력되지 않습니다.

Django는 이용자가 업로드한 파일은 MEDIA_URL과 MEDIA_ROOT라는 설정값을 참조하여 제공(serve)합니다.



## 부록

### (1) url 함수의 kwargs 역할

url 함수에 사용되는 인자인 kwargs는 뷰 함수로 임의 인자를 건내는 데 사용됩니다.

뷰 함수는 URL 패턴에서 지정된 값을 인자로 건내받는데, URL에는 어떤 상태나 정보를 나타내지 않으면서 상황에 따라 뷰 함수에 넘기는 값을 따로 지정하려면 kwargs 인자를 활용해야 합니다. 


예를 들어, 개별 사진을 /photos/<숫자ID>/이나 /hidden-photos/<숫자ID>/ URL로 접근할 수 있고, 두 URL 모두 detail 함수가 대응한다고 가정하겠습니다. 어떤 URL로 접근했는지 detail 함수에서 알려면 접근한 URL을 분석해도 되지만, URL엔 보이지 않는 정보를 detail 함수에 인자로 보내면 좀 더 편할 겁니다. 이 인자를 hidden이라고 하겠습니다. 먼저 urls.py에 kwargs 인자를 정의합니다.


### (2) render와 HttpResponse

views.py를 처음 열면 맨 위에 from django.shortcuts import render라는 부분이 있습니다. 그런데 우리는 이 render 함수를 한 번도 쓰지 않고, HttpResponse를 따로 불러들여서 이를 이용해 화면에 뭔가를 출력했습니다. 


#### [차이점]


HttpResponse는 Django의 View가 HTTP handler로 보내는 출력물의 가장 기본 형태인 객체를 만드는 클래스입니다. HTTP handler가 건내받는 출력물의 가장 기본형이지요. 그래서 HttpResponse 자체는 템플릿을 같은 걸 처리하는 기능을 담고 있지 않습니다. 

그래서 템플릿을 따로 처리하여 그려낸(rendered) 출력물을 문자열 그 자체(plain text)로 받아서 출력해야 합니다. 이런 처리에 필요한 코드는 꽤 반복되므로 반복되는 부분을 별도 함수로 만들어서 편하게 템플릿으로 그려낸 출력물을 HttpResponse로 보내는 함수가 바로 render입니다. render 함수를 보면 반환하는 최종 값도 결국은 HttpResponse 클래스로 만든 객체입니다.