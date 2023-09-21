using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
 * C# 자료형 종류
 * // 정수
 * - byte (1 byte)
 * - sbyte (1 byte)
 * 
 * - short (2 byte)
 * - ushort (2 byte)
 * 
 * - int (4 byte)
 * - uint (4 byte)
 * 
 * - long (8 byte)
 * - ulong (8 byte)
 * 
 * // 실수
 * - float (4 byte)
 * - double (8 byte)
 * - decimal (16 byte)
 * 
 * // 문자
 * - char (2 byte)
 * 
 * // 기타
 * - object
 * - string
 * - class
 * - struct
 * 
 * C# 자료형 형식
 * - 값 형식
 * - 참조 형식
 * 
 * C# 자료형은 크게 값 형식 자료형과 참조 형식 자료형으로 구분된다.
 * 
 * 값 형식 자료형이란?
 * - 값 형식 자료형은 데이터 자체를 다루기 때문에 값 형식 자료형 변수를 다른 변수에 할당하면 원본과 상관없는 완전한 사본이
 * 만들어진다. (즉, 사본 변수를 변경해도 원본 변수에는 영향을 미치지 않는다는 것을 알 수 있다.)
 * 
 * 또한, 값 형식 자료형은 시스템에 의해서 메모리가 관리되는 특징이 존재하기 때문에 사용자 (프로그래머) 가 메모리 관리에
 * 신경 쓸 필요가 없다는 장점이 존재한다.
 * 
 * 참조 형식 자료형이란?
 * - 참조 형식 자료형은 데이터를 지니고 있는 대상의 참조 값을 다루기 때문에 참조 형식 자료형 변수를 다른 변수에 할당하면
 * 얕은 복사가 발생한다. (즉, 완전한 사본이 만들어지는 것이 아니기 때문에 사본 변수를 변경하면 원본 변수도 영향을 받는다는
 * 것을 알 수 있다.)
 * 
 * 또한, 참조 형식 자료형은 시스템에 의해서 메모리가 관리되는 값 형식과 달리 가비지 컬렉션에 의해서 메모리가 관리된다. (즉, 
 * 가비지 컬렉션이 존재하기 때문에 참조 형식 자료형도 자동으로 메모리가 관리되지만 가비지 컬렉션이 너무 많이 동작 할 경우
 * 프로그램의 성능이 저하되는 단점이 존재한다.)
 * 
 * 기본 자료형은 포함한 구조체가 값 형식 자료형에 속하면 해당 자료형은 제외한 나머지 자료형은 참조 형식 자료형에 속한다.
 * 
 * object 자료형이란?
 * - C# 의 모든 자료형이 상속 받는 최상위 자료형을 의미한다. (즉, C# 의 모든 자료형은 반드시 object 자료형을 직/간접적으로
 * 상속한다는 특징이 존재한다.)
 * 
 * 따라서, object 자료형을 활용하면 C# 에 존재하는 모든 데이터를 저장 및 제어하는 것이 가능하다. (즉, 다형성에 의해서 부모
 * 클래스 자료형 변수로 자식 클래스 객체를 참조하는 것이 가능하다는 것을 알 수 있다.)
 * 
 * 단, object 자료형은 참조 형식 자료형에 속하기 때문에 해당 자료형 변수에 값 형식 데이터를 할당 할 경우 내부적으로 Boxing
 * 이 발생한다는 단점이 존재한다.
 * 
 * Boxing 발생하면 내부적으로 추가적인 메모리 할당이 발생하며 해당 메모리는 가비지 컬렉션에 의해서 관리 된다는 특징이
 * 존재한다. (즉, Boxing 이 많이 일어날 수록 추가적인 메모리가 할당되며 이는 곧 가비지 컬렉션이 동작을 유발시킨다는 것을
 * 알 수 있다.)
 * 
 * 따라서, object 자료형을 사용 할 경우 가능하면 참조 형식 데이터만을 할당하는 것이 좋은 습관이라는 것을 알 수 있다.
 */
namespace E01 {
	/** Example 5 */
	public partial class CE01Example_05 : CE01SceneManager {
		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_05;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();

			/*
			 * C# 은 강력 형식 언어 (Strong Type Language) 이기 때문에 특정 데이터를 사용하기 위해서는 반드시 해당 데이터가
			 * 어떤 자료형의 데이터인지 명시 할 필요가 있다.
			 * 
			 * 따라서, 특정 데이터를 변수에 할당하기 위해서는 가능하면 변수의 자료형과 동일한 자료형 데이터를 할당하는 것이
			 * 좋은 습관이다.
			 */
			byte nByte01 = byte.MaxValue;
			sbyte nByte02 = sbyte.MaxValue;

			/*
			 * signed vs unsigned
			 * - signed 자료형은 부호가 존재하는 자료형을 의미한다. (즉, 부호가 존재하기 때문에 양수 뿐만 아니라 음수를
			 * 표현하는 것이 가능하다.)
			 * 
			 * 단, signed 자료형은 음수를 표현하기 위해 1 비트를 희생하기 때문에 표현 할 수 있는 값의 범위가 절반으로
			 * 줄어드는 단점이 존재한다.
			 * 
			 * 반면, unsigned 자료형은 부호가 없는 자료형을 의미한다. (즉, 부호가 없기 때문에 음수를 표현하는 것이
			 * 불가능하다는 것을 알 수 있다.)
			 * 
			 * unsigned 자료형은 음수를 표현 할 수 없지만 부호 비트 또한 값을 표현하는데 활용되기 때문에 signed 자료형에
			 * 비해서 표현 할 수 있는 값의 범위가 2 배가 된다는 장점이 존재한다.
			 */
			short nShort01 = short.MaxValue;
			ushort nShort02 = ushort.MaxValue;

			int nInt01 = int.MaxValue;
			uint nInt02 = uint.MaxValue;

			long nLong01 = long.MaxValue;
			ulong nLong02 = ulong.MaxValue;

			/*
			 * Debug.Log 계열 메서드는 문자열을 Unity 로그 뷰에 출력하는 역할을 수행한다. (즉, 해당 메서드를 활용하면
			 * 프로그램이 실행 중에 특정 메세지를 출력하는 것이 가능하다는 것을 알 수 있다.)
			 */
			Debug.Log("=====> 정수 <=====");
			Debug.Log($"byte : {nByte01}, {nByte02}");
			Debug.Log($"short : {nShort01}, {nShort02}");
			Debug.Log($"int : {nInt01}, {nInt02}");
			Debug.Log($"long : {nLong01}, {nLong02}");

			/*
			 * float 와 double 자료형은 부동 소수점 방식을 사용해서 소수점을 표현하며 decimal 자료형은 고정 소수점 방식을
			 * 사용하는 차이점이 존재한다.
			 * 
			 * 부동 소수점 vs 고정 소수점
			 * - 부동 소수점은 상대적으로 적은 비트를 가지고 넓은 범위의 값을 표현 할 수 있다는 장점이 존재하지만 값의
			 * 정밀도가 떨어진다는 단점이 존재한다. (즉, 부동 소수점을 통해서 표현되는 데이터를 미세한 오차가 존재한다는
			 * 것을 알 수 있다.)
			 * 
			 * 반면, 고정 소수점 방식은 값을 정확하게 표현하는 것이 가능하지만 값을 표현하기 위해서 많은 비트가 필요하며
			 * 데이터의 연산 속도가 떨어진다는 단점이 존재한다. (즉, 부동 소수점 방식은 대부분의 컴퓨터에서 사용되는 방식이기
			 * 떄문에 부동 소수점을 빠르게 계산하기 위한 FPU 가 존재하지만 고정 소수점 방식은 연산을 빠르게 수행하기 위한
			 * 하드웨어가 별도로 존재하지 않는다는 것을 알 수 있다.)
			 */
			float fFloat = float.MaxValue;
			double dblDouble = double.MaxValue;
			decimal dmDecimal = decimal.MaxValue;

			Debug.Log("=====> 실수 <=====");
			Debug.Log($"float : {fFloat}");
			Debug.Log($"double : {dblDouble}");
			Debug.Log($"decimal : {dmDecimal}");

			/*
			 * object 자료형은 C# 에 존재하는 모든 자료형이 직/간접적으로 상속하는 최상위 자료형이기 때문에 해당 자료형을
			 * 활용하면 C# 에 존재하는 모든 자료형의 데이터를 저장 및 관리 할 수 있다는 것을 알 수 있다.
			 * 
			 * 단, 해당 자료형 변수로부터 데이터를 읽어 들일 때는 반드시 특정 자료형으로 형 변환해줘야한다. (즉, 잘못된
			 * 자료형으로 형변환 할 경우 프로그램이 오작동 한다는 것을 알 수 있다.)
			 * 
			 * Ex)
			 * object oObj = 10;
			 * int nVal = (int)oObj;
			 */
			object oObj = 10;
			string oStr = "Hello, World!";

			Debug.Log("=====> 기타 <=====");
			Debug.Log($"object : {oObj}");
			Debug.Log($"string : {oStr}");
		}
		#endregion // 함수
	}
}