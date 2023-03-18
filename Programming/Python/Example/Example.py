"""
import 키워드는 특정 Python 모듈을 포함 시키는 역할을 수행한다.
"""
import os
import sys

from Classes.Example_03.CExample_03 import *
from Classes.Example_04.CExample_04 import *
from Classes.Example_05.CExample_05 import *
from Classes.Example_06.CExample_06 import *
from Classes.Example_07.CExample_07 import *
from Classes.Example_09.CExample_09 import *
from Classes.Example_10.CExample_10 import *
from Classes.Example_11.CExample_11 import *
from Classes.Example_12.CExample_12 import *
from Classes.Example_13.CExample_13 import *
from Classes.Example_14.CExample_14 import *
from Classes.Example_15.CExample_15 import *

"""
Python 프로젝트 주제
- Example_03 (Python 기초)
- Example_04
- Example_05
- Example_06
- Example_07
- Example_09
- Example_10
- Example_11
- Example_12
- Example_13
- Example_14
- Example_15
"""

"""
주석이란?
- 컴파일러에 의해서 해석되지 않는 구문을 의미한다. (즉, 주석을 활용하면 명령문의 특정 부분을 비활성화하는 것이 가능하다.)

주석은 컴파일러에 의해서 해석되는 명령문이 아니라 사용자 (프로그래머) 를 위해서 제공되는 기능으로서 메모 용도로 주로 활용된다.
복잡한 명령문을 작성 후 오랜 시간이 지나면 해당 명령문을 작성했던 사용자도 다시 해석을 해야 될 필요가 있기 때문에 이때 주석을 활용해서
명령문에 대한 부가적인 설명을 작성해놓으면 명령문을 다시 해석하는데 들어가는 시간을 줄이는 것이 가능하다.

주석 종류
- 단일 행 주석
- 다중 행 주석

단일행 주석은 한 줄을 주석 처리하는 기능을 의미하며 다중행 주석은 여러 줄을 주석 처리하는 기능을 의미한다.
단, Python 은 다중행 주석을 지원하지 않기 때문에 문자열을 이용해서 메모를 남기는 용도로 활용한다.

메인 모듈이란?
- Python 은 프로그램이 실행 될 때 가장 처음 실행 할 진입 함수 (메서드) 가 따로 존재하지 않는다.
따라서, 어떤 파일이 먼저 실행되느냐에 따라 결과가 달라지기 때문에 사용자 (프로그래머) 가 임의적으로 진입 함수를 만들어 줄 필요가 있다.

Python 인터프리터는 가장 먼저 실행되는 파일의 모듈 이름을 __main__ 으로 지정하기 때문에 해당 특징을 활용하면 진입 함수 역할을 하는
파일을 제작하는 것이 가능하다.
"""
# 메인 모듈 일 경우
if __name__ == "__main__":
    CExample_03.Start(sys.argv)
    # CExample_04.Start(sys.argv)
    # CExample_05.Start(sys.argv)
    # CExample_06.Start(sys.argv)
    # CExample_07.Start(sys.argv)
    # CExample_09.Start(sys.argv)
    # CExample_10.Start(sys.argv)
    # CExample_11.Start(sys.argv)
    # CExample_12.Start(sys.argv)
    # CExample_13.Start(sys.argv)
    # CExample_14.Start(sys.argv)
    # CExample_15.Start(sys.argv)
    