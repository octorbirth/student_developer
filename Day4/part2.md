# 개발 환경 꾸리기

## Python 설치
(1) Mac OS, Linux

Python 설치

<pre><code>python --version</code></pre>
<pre><code>brew install python3</code></pre>

Homebrew가 설치되어 있지 않다면 brew부터 설치해야 하며,
brew 설치할 때 xcode 관련 도구인 Command Line Tools가 요구되기도 합니다.
대개는 관련 과정이 함께 안내되는데, 실수로 그냥 넘어갔거나 안내되지 않았다면
다음 명령어로 Command Line Tools를 설치하면 됩니다.

<pre><code>xcode-select --install</code></pre>
<pre><code>sudo apt-get install python3</code></pre>


(2) Windows

제가 Mac OS를 사용하다 보니 Windows 환경에서 Python을 설치하는 방법에 관해서는 설명하기 어렵습니다.


### (2) virtualenv 설치

<code> python3 -m venv  </code>
                                       

### (3) SQLite 설치

데이터를 저장하는 데 필요한 데이터베이스는 SQLite를 사용할 겁니다.
Mac OS나 Linux 계열 운영체제엔 SQLite 3가 보통은 이미 설치되어 있습니다.

<code>sqlite3</code>

그래서 SQLite 3 설치를 신경써야 하는 경우는 흔하지 않으며, 여러분이 SQLite 3이 설치되어 있지 않아서 문제를 겪는 경우도 드뭅니다. 하지만 그 드문 일을 대비해 설치하는 과정을 다루겠습니다.

Mac OS에서는 Homebrew로 설치하거나 버전 업그레이드를 하면 편합니다.

<pre><code>brew update
brew upgrade
brew install sqlite3
brew link --force sqlite
</pre></code>

하지만 이미 sqlite3이 설치되어 있다는 경고가 표시되며 설치되지 않을 겁니다.
이미 설치되어 있을 테니까요.

그런데 패키지 관리 도구로 설치가 안 되거나 직접 소스를 직접 컴파일하여 설치하고 싶다면 sqlite.org의 Download 페이지에 가서 “Source Code” 영역에 있는 sqlite-autoconf로 이름이 시작하는 파일을 받습니다. 파일 확장자는 tar.gz입니다. 이 소스 파일을 다음과 같이 컴파일하여 설치하면 됩니다.


### (4) Django 설치
가상 환경 생성과 진입

이제 드디어 Django를 설치할 차례입니다. virtualenv로 가상 환경을 만들고 그곳에 Django를 설치하겠습니다.

<code>python3 -m venv env_pystagram</code>

python3에 내장된 venv를 이용하여 env_pystagram라 이름 붙인 가상 환경을 만드는 명령입니다.
잠깐 멈칫하다가 env_pystagram 이름으로 된 디렉터리가 만들어집니다.

Python 가상 환경을 활성화하려면 Python 가상 환경 디렉터리 안에 있는 파일을 이용해야 합니다. Mac OS나 Linux 계열에선 다음 명령어를 실행합니다.

<code>source env_pystagram/bin/activate</code>

env_pystagram 디렉터리 안에 있는 bin 디렉터리에 activate 파일을 이용한 겁니다. Windows에선 다음 명령어를 실행합니다.

<code>env_pystagram\Scripts\activate.bat</code>

env_pystagram 디렉터리 안에 있는 Scripts 디렉터리의 activate.bat 파일을 실행한 겁니다.

가상 환경에 잘 진입하면 쉘 프롬프트에 가상 환경 이름이 덧붙어 표시됩니다.

가상 환경에서 빠져 나오려면 deactivate 명령어를 실행하세요. 그러면 쉘 프롬프트에 (pystagram) 부분이 표시되지 않는데, pystagram이라 이름 붙인 가상 환경에서 빠져 나와서 그렇습니다.


### (4) 편리한 도구 설치

Pystagram을 만드는 데 필요한 Python 패키지는 그때그때 설치하겠습니다. 
(1) Postman - REST Client

Postman - REST Client는 HTTP 기반으로 동작하는 API를 편리하게 호출하는 클라이언트(client)입니다. 서버에 기능을 구현한 후 동작 여부를 확인하려면 클라이언트에서 접근할 수 있는 인터페이스(interface)를 만들어야 합니다.
이 클라이언트쪽 인터페이스를 만드는 것 자체가 귀찮기도 하지만, 오류를 확인하고 추적하는 디버깅(debuging) 환경이 미비하여 문제를 파악하기도 불편합니다.
Postman은 개발에 용이한 클라이언트 인터페이스를 제공하는 도구입니다.

(2) 편집기

프로그래밍은 해본 적이 없고 정말 Python 등으로 Hello world만 출력해본 분이라면 코딩에 필요한 편집기를 아직 결정하지 못하셨을 겁니다.
Django로 프로그래밍을 하는 데 필요한 전용 편집기는 따로 없습니다.
편집기는 다양하며 취향에 맞는 걸 쓰면 됩니다.

* Atom (무료)
* Notepad (일명 메모장. 유료 운영체제에 기본 내장)
* PyCharm (무료, 유료)
* Sublime Text (유료)
* Vim (무료)

### (5) Python

* 들여쓰기

Python의 언어 문법은 코드를 들여 쓰는 규칙(indentation)을 엄격히 따릅니다.
같은 맥락에 있는 코드는 들여 쓰는 깊이가 같아야 합니다. 들여 쓰는 깊이는 탭(tab)으로 만드는데, 이 탭은 한 자리 공백(space) 문자로 표현하는 소프트 탭(soft tab) 방식과 자판에 있는 탭 키로 표현하는 하드 탭(hard tab) 방식이 있습니다.

Python Package : 모듈은 함수나 변수, 클래스를 모아 놓은 파일이며, 패키지는 모듈을 묶어놓은 것이다.