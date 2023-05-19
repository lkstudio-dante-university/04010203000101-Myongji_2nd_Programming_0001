import os
import sys


# Example 3
class CExample_03:
	"""
	@classmethod 키워드는 해당 메서드가 객체에 종속되는 맴버 메서드가 아니라 클래스에 종속되는 클래스 메서드라는 것을 Python
	인터프리터에게 알리는 역할을 수행한다.

	따라서, 해당 키워드로 명시된 메서드는 클래스를 이름을 통해서 호출하는 것이 가능하며 항상 첫번째 매개 변수로 클래스 자체를
	나타내는 참조가 전달된다. (즉, 해당 매개 변수 이름은 cls 를 사용하는 것이 관례이며 맴버 메서드 일 경우에는 self 를 사용한다.)
	"""
	
	# 초기화
	@classmethod
	def Start(cls, args):
		"""
		input 메서드란?
		- 콘솔 창으로부터 데이터를 입력 받는 역할을 수행한다.

		해당 메서드를 활용하면 프로그램이 실행 중에 필요한 데이터를 사용자로부터 입력을 받는 것이 가능하기 때문에 print 메서드와 더불어 콘솔
		프로그램에서 가장 많이 활용되는 메서드 중 하나이다.

		split 메서드란?
		- 주로 문자열 데이터를 특정 문자를 기준으로 분할 시킬 때 활용되는 메서드이다. 또한, 해당 메서드는 반환 값으로 리스트 형 데이터를
		반환하기 때문에 해당 결과를 활용하면 분할 된 데이터를 손쉽게 제어하는 것이 가능하다.
		"""
		oTokenList = input("수식 입력 : ").split()
		
		"""
		len 메서드란?
		- 특정 컬렉션 데이터에 저장 된 요소의 개수를 반환하는 역할을 수행한다. (즉, 해당 메서드를 활용하면 문자열 뿐만 아니라 다양한 컬렉션의
		길이 (요소 개수) 를 계산하는 것이 가능하다.)
		"""
		if len(oTokenList) >= 3:
			nLhs = int(oTokenList[0])
			nRhs = int(oTokenList[2])
			
			"""
			print 메서드란?
			- 입력으로 전달 된 데이터를 콘솔 창에 출력하는 역할을 수행한다.
			
			해당 메서드는 문자열을 비롯한 숫자형 등 모든 자료형 데이터를 출력하는 것이 가능하기 때문에 다른 고수준 언어처럼 복잡한 문법과 규칙을
			몰라도 손쉽게 원하는 데이터를 출력하는 것이 가능하다.
			"""
			print("\n=====> 수식 입력 결과 <=====")
			
			"""
			문자열 포맷팅이란?
			- 문자열을 비롯한 여러 데이터를 활용해서 문자열을 생성 할 수 있는 기능을 의미한다. (즉, 문자열 포맷팅을 활용하면 다양한 데이터를
			이용해서 단어 또는 문장을 구성하는 것이 가능하다.)

			Ex)
			nVal = 10
			fVal = 3.14

			f"정수 : {nVal}, 실수 : {fVal}"		<= 정수 : 10, 실수 : 3.14
			"""
			# + 일 경우
			if oTokenList[1] == "+":
				print(f"{nLhs} + {nRhs} = {nLhs + nRhs}")
			
			# - 일 경우
			elif oTokenList[1] == "-":
				print(f"{nLhs} - {nRhs} = {nLhs - nRhs}")
			
			# * 일 경우
			elif oTokenList[1] == "*":
				print(f"{nLhs} * {nRhs} = {nLhs * nRhs}")
			
			# / 일 경우
			elif oTokenList[1] == "/":
				print(f"{nLhs} / {nRhs} = {nLhs / nRhs}")