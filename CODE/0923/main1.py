# 모듈
'''
    모듈
    파이썬 코드가 저장된 파일
    함수, 변수, 클래스 등을 모아놓은 파일로 다른 프로그램에서 가져다 쓸 수 있음

    도구상자: 여러 도구(함수)를 모아둔 상자(모듈)
    레고 블록: 필요한 블록(모듈)을 가져와서 조립
    요리 레시피: 필요한 레시피(모듈)를 참고해서 요리
'''

# 코드 재사용: 한 번 작성한 코드를 여러 곳에서 사용
# 유지 보수: 기능별로 분리하여 관리가 쉬움
# 협업: 팀원들과 코드 공유가 편리
# 네임스페이스: 이름 충돌 방지

# 전체 모듈 가져오기
import calculator1

result = calculator1.add(10, 5)
print(result)

# 작성되어 있는 모듈
import math as m # 별칭
import random
import datetime

print(m.pi)
print(random.randint(1, 11))
print(datetime.datetime.now())

# 패키지(Package)
'''
    패키지(Package)는 모듈들을 모아놓은 디렉토리
    관련된 모듈들을 체계적으로 관리 가능
'''
from mypackage import module1
from mypackage import module2

module1.greet()
module2.hello()

from mypackage.module1 import greet
from mypackage.module2 import hello

greet()
hello()

# 가상환경(새로운 공간)
# 프로젝트별로 독립적인 패키지 환경을 만들 수 있음

# 가상환경 생성
# python3 -m venv 이름(myenv)

# 가상환경 활성화(Window)
# myenv\Scripts\activate

# 가상환경 활성화(Mac/Linux)
# source myenv/bin/activate

# 가상환경 비활성화
# deactivate

# pip
# 파이썬 패키지 관리자






