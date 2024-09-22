using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
 * Unity 란?
 * - 멀티 (크로스) 플랫폼을 지원하는 멀티 미디어 프로그램을 제작 할 수 있는 툴을 의미한다. (즉, Unity 의 주요 분야는
 * 게임이지만 게임 이외에도 컴퓨터 그래픽스가 필요한 다양한 분야에 활용 된다는 것을 알 수 있다.)
 * 
 * Unity 주요 기능
 * - 스크립트 지원
 * - 애니메이션 지원
 * - 렌더링 지원
 * - 파티클 시스템 지원
 * - 사운드 지원
 * - 물리 엔진 지원 (PhysicX, Box2D)
 * - UI 시스템 지원
 * - 리소스 (에셋) 관리 기능 지원
 * 
 * Unity 는 렌더링을 비롯한 게임을 제작하기 위한 핵심 기능을 제공하기 때문에 Unity 를 활용하면 다양한 프로그램을 손쉽게
 * 제작하는 것이 가능하다.
 * 
 * Unity 관련 주요 용어
 * - 컴포넌트
 * - 게임 객체
 * - 씬
 * - 에셋
 * 
 * 컴포넌트란?
 * - 특정 역할을 수행하는 기능을 의미한다. 컴포넌트는 단독으로 사용하는 것은 불가능하며 특정 컴포넌트를 게임 객체에
 * 추가함으로서 컴포넌트를 동작시키는 것이 가능하다. (즉, 컴포넌트를 게임 객체에 추가함으로서 여러가지 사물을 표현하는 것이
 * 가능하다.)
 * 
 * 게임 객체란?
 * - 컴포넌트를 추가하기 위한 그릇을 의미한다. (즉, 게임 객체 자체는 아무런 역할도 없지만 해당 객체에 컴포넌트를 추가함으로서
 * 다양한 역할을 수행하는 사물을 표현하는 것이 가능하다.)
 * 
 * Unity 는 컴포넌트 기반 프로그래밍 방식을 지원하며 게임 객체에 여러 컴포넌트를 추가 시킴으로서 특정 역할을 수행하는 사물을
 * 제작하는 것이 가능하다.
 * 
 * 씬이란?
 * - 게임 객체를 배치할 수 있는 가상의 공간을 의미한다. (즉, Unity 의 모든 객체는 씬 상에 배치 된다는 것을 알 수 있다.)
 * 
 * Unity 로 제작 된 프로그램은 반드시 1 개 이상의 씬을 포함하고 있어야 하며 특정 물체를 씬 상에 배치 함으로서 사용자에게
 * 보여 줄 장면을 구성하는 것이 가능하다.
 * 
 * 에셋이란?
 * - 이미지와 같은 프로그램을 제작하기 위해서 사용되는 여러 자원을 의미한다. 
 * 
 * Unity 는 이미지와 같은 파일을 인식하기 위해서 자동으로 메타 파일을 생성하며 메타 파일과 리소스 파일을 묶어서 에셋이라고 
 * 지칭한다. (즉, Unity 에서 이미지와 같은 리소스를 사용하기 위해서는 반드시 해당 리소스와 쌍을 이루는 메타 파일이 필요하다는
 * 것을 알 수 있다.)
 */
namespace Example
{
	/** Example 1 */
	public partial class CE01Example_01 : CSceneManager
	{
		#region 프로퍼티
		public override string SceneName => KDefine.G_N_SCENE_EXAMPLE_01;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake()
		{
			base.Awake();
		}
		#endregion // 함수
	}
}