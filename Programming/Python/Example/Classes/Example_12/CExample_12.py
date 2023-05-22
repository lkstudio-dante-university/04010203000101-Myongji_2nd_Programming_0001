import os
import sys

from PyQt5 import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# Example 12
class CExample_12(QMainWindow, uic.loadUiType("Resources/Example_12/E12MainWindow.ui")[0]):
	# 생성자
	def __init__(self):
		# 멤버를 설정한다
		self.m_oKeySet = set()
		
		super().__init__()
		self.__init__example_12__()
	
	# 초기화
	def __init__example_12__(self):
		self.show()
		self.setupUi(self)
		self.setWindowTitle("Example 12")
		
		# 영역을 설정한다
		nHeight = self.frameGeometry().height() - self.geometry().height()
		self.setGeometry(10, 10 + nHeight, self.geometry().width(), self.geometry().height())
		
		# 타이머를 설정한다
		self.m_oTimer = QTimer(self)
		self.m_oTimer.timeout.connect(self.OnUpdate)
		
		self.m_oTimer.start()
		
		# 메뉴 바를 설정한다
		self.menuBar().setNativeMenuBar(False)
		self.actionAbout.triggered.connect(self.OnClickAboutMenu)
	
	# 상태를 갱신한다
	def OnUpdate(self):
		self.update()
	
	# 그리기 이벤트를 수신했을 경우
	def paintEvent(self, a_oEvent: QPaintEvent):
		oPainter = QPainter(self)
		
		try:
			pass
		
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
		
		self.m_oKeySet.add(a_oEvent.key())
	
	# 키 눌림 종료 이벤트를 수신했을 경우
	def keyReleaseEvent(self, a_oEvent: QKeyEvent):
		self.m_oKeySet.remove(a_oEvent.key())
	
	# 정보 메뉴를 눌렀을 경우
	def OnClickAboutMenu(self):
		QMessageBox.aboutQt(self, "알림")
	
	# 초기화
	@classmethod
	def Start(cls, args):
		oApp = QApplication(args)
		oExample = CExample_12()
		
		sys.exit(oApp.exec())
