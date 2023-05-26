import os
import sys
import math
import random

from PyQt5 import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Practice.Classes.Practice_12.CP12Shape import *

from Example.Classes.Global.Manager.CTimeManager import *
from Example.Classes.Global.Manager.CInputManager import *

"""
과제 12 - 1
- PyQt 를 이용한 볼 반사 프로그램 제작하기
- 프로그램 시작 시 볼 1 개 랜덤한 방향으로 움직인다
- 볼은 화면 끝에 도착했을 경우 반사 되어 방향을 변경한다
- 즉, 왼쪽 또는 오른쪽 끝에 도착했을 경우 x 방향이 변화되며 위쪽 또는 아래쪽 끝에 도착했을 경우 y 방향이 변화된다.
"""


# Practice 12
class CPractice_12(QMainWindow, uic.loadUiType("Resources/Practice_12/P12MainWindow.ui")[0]):
	# 생성자
	def __init__(self):
		# 멤버 변수를 설정한다
		self.m_oCircleList = []
		
		super().__init__()
		self.__init__practice_12__()
	
	# 초기화
	def __init__practice_12__(self):
		self.show()
		self.setupUi(self)
		self.setWindowTitle("Practice 12")
		
		# 영역을 설정한다
		nHeight = self.frameGeometry().height() - self.geometry().height()
		self.setGeometry(10, 10 + nHeight, self.geometry().width(), self.geometry().height())
		
		# 타이머를 설정한다
		self.m_oTimer = QTimer(self)
		self.m_oTimer.timeout.connect(self.OnUpdate)
		
		self.m_oTimer.start(1)
		
		# 메뉴 바를 설정한다
		self.menuBar().setNativeMenuBar(False)
		self.actionAbout.triggered.connect(self.OnClickAboutMenu)
		
		# 도형을 설정한다
		fAngle = random.random() * 360.0
		
		oCircle = CP12Circle(150.0)
		oCircle.SetPos(QPointF(self.geometry().width() / 2.0, self.geometry().height() / 2.0))
		oCircle.SetDirection(QPointF(math.cos(math.radians(fAngle)), math.sin(math.radians(fAngle))))
		
		self.m_oCircleList.append(oCircle)
	
	# 상태를 갱신한다
	def OnUpdate(self):
		self.update()
		
		# 스페이스 키를 눌렀을 경우
		if CInputManager.GetInst().IsKeyPress(Qt.Key_Space):
			oCircleList = []
			
			for oCircle in self.m_oCircleList:
				# 최소 크기 일 경우
				if oCircle.GetRadius() <= 15.0:
					oCircleList.append(oCircle)
					
				else:
					for i in range(0, 2):
						fAngle = random.random() * 360.0
						
						oSubCircle = CP12Circle(max(15.0, oCircle.GetRadius() / 2.0))
						oSubCircle.SetPos(oCircle.GetPos())
						oSubCircle.SetDirection(QPointF(math.cos(math.radians(fAngle)), math.sin(math.radians(fAngle))))
						
						oCircleList.append(oSubCircle)
						
			self.m_oCircleList = oCircleList
		
		# 위치를 갱신한다
		for oCircle in self.m_oCircleList:
			oNextPos = oCircle.GetPos() + (oCircle.GetDirection() * 350.0) * CTimeManager.GetInst().GetDeltaTime()
			oNextPos.setX(max(oNextPos.x(), oCircle.GetRadius()))
			oNextPos.setX(min(oNextPos.x(), self.geometry().width() - oCircle.GetRadius()))
			
			oNextPos.setY(max(oNextPos.y(), oCircle.GetRadius() + self.menuBar().geometry().height()))
			oNextPos.setY(min(oNextPos.y(), self.geometry().height() - oCircle.GetRadius()))
			
			# 왼쪽 or 오른쪽 영역을 벗어났을 경우
			if oNextPos.x() <= oCircle.GetRadius() or oNextPos.x() >= self.geometry().width() - oCircle.GetRadius():
				oCircle.SetDirection(QPointF(oCircle.GetDirection().x() * -1.0, oCircle.GetDirection().y()))
			
			# 위쪽 or 아래쪽 영역을 벗어났을 경우
			if oNextPos.y() <= oCircle.GetRadius() + self.menuBar().geometry().height() or oNextPos.y() >= self.geometry().height() - oCircle.GetRadius():
				oCircle.SetDirection(QPointF(oCircle.GetDirection().x(), oCircle.GetDirection().y() * -1.0))
			
			oCircle.SetPos(oNextPos)
			
		# 관리자를 갱신한다
		CTimeManager.GetInst().Update()
		CInputManager.GetInst().Update()
		
		# 라벨을 갱신한다
		self.labelDeltaTime.setText("Delta Time: {0:0.5f} sec".format(CTimeManager.GetInst().GetDeltaTime()))
		self.labelRunningTime.setText("Running Time: {0:0.5f} sec".format(CTimeManager.GetInst().GetRunningTime()))
	
	# 그리기 이벤트를 수신했을 경우
	def paintEvent(self, a_oEvent: QPaintEvent):
		oPainter = QPainter(self)
		
		try:
			for oCircle in self.m_oCircleList:
				oCircle.Draw(oPainter)
		
		finally:
			oPainter.end()
	
	# 닫기 이벤트를 수신했을 경우
	def closeEvent(self, a_oEvent: QCloseEvent):
		nResult = QMessageBox.question(self, "알림", "앱을 종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		a_oEvent.accept() if nResult == QMessageBox.Yes else a_oEvent.ignore()
	
	# 키 눌림 이벤트를 수신했을 경우
	def keyPressEvent(self, a_oEvent: QKeyEvent):
		# Esc 키를 눌렀을 경우
		if a_oEvent.key() == Qt.Key_Escape:
			self.close()
			
		CInputManager.GetInst().AddKey(a_oEvent.key())
		
	# 키 눌림 종료 이벤트를 수신했을 경우
	def keyReleaseEvent(self, a_oEvent: QKeyEvent):
		CInputManager.GetInst().RemoveKey(a_oEvent.key())
	
	# 정보 메뉴를 눌렀을 경우
	def OnClickAboutMenu(self):
		QMessageBox.aboutQt(self, "알림")
	
	# 초기화
	@classmethod
	def Start(cls, args):
		oApp = QApplication(args)
		oPractice = CPractice_12()
		
		sys.exit(oApp.exec())
