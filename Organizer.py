# -*-coding:cp949-*-
##################################################
# program: Organizer.py
# author: Pingvino Kay
# version: 0.8
# date: 13/08/29
##################################################
import sys
import os
import datetime
import tkinter.ttk
def organize(x=0, y=False):
	for i in os.listdir():
		if i == os.path.basename(sys.argv[0]):
			pass
		elif x == 0:
			if os.path.isfile(i) == True:  # 파일일 경우 확장자별로 분류해 정리한다.
				if os.path.splitext(i)[1] != '':  # 확장자가 없을 경우는 따로 폴더를 만들어 정리한다.
					os.renames(i, os.path.abspath(os.path.splitext(i)[1] + '\\' + i))
				else:
					os.renames(i, os.path.abspath('확장자 없음\\' + i))
			else:
					os.renames(i, os.path.abspath("폴더\\" + i))
		elif x == 1:
			os.renames(i, os.path.abspath(datetime.datetime.fromtimestamp(float(os.stat(i)[7])).strftime('%Y-%m-%d') + '\\' + i))  # 만든 날짜별로 정리한다.
		elif x == 2:
			os.renames(i, os.path.abspath(datetime.datetime.fromtimestamp(float(os.stat(i)[8])).strftime('%Y-%m-%d') + '\\' + i))  # 수정한 날짜별로 정리한다.
		elif x == 9:
			y = False
			for i in os.listdir():  # 원래대로 되돌린다.
				if i == os.path.basename(sys.argv[0]):
					pass
				elif os.path.isdir(i) == True:
					if os.listdir(i) == []:
						pass
					else:
						for j in os.listdir(i):
							os.rename(os.path.abspath(i + '\\' + j), os.path.abspath(j))
						os.rmdir(i)
				else:
					pass
		else:
			pass
	if y == True:
		for i in os.listdir():
			if i == os.path.basename(sys.argv[0]):
				pass
			else:
				os.renames(i, os.path.abspath('Organized\\' + i))
	else:
		pass
class MyApp:
	def __init__(self, parent):
		self.myParent = parent
		self.v0 = tkinter.IntVar()
		self.v1 = tkinter.BooleanVar()
		self.n = tkinter.ttk.Notebook(parent)
		self.n.pack()
		self.myC1 = tkinter.Frame(self.n)  # 확장자별로 정리하는 라디오 버튼이 들어갈 프레임.
		self.myC1.pack()
		self.myC2 = tkinter.Frame(self.n)  # 시간별로 정리하는 라디오 버튼이 들어갈 프레임.
		self.myC2.pack()
		self.myC3 = tkinter.Frame(self.n)  # 정리된 폴더를 원래대로 되돌릴 라디오 버튼이 들어갈 프레임.
		self.myC3.pack()
		self.myCy = tkinter.Frame(parent)
		self.myCy.pack()
		self.myCx = tkinter.Frame(parent)  # 버튼이 들어갈 프레임.
		self.myCx.pack()
		self.R1 = tkinter.Radiobutton(self.myC1, text='확장자별로 정리합니다.', variable=self.v0, value=0)
		self.R1.pack()
		self.R2 = tkinter.Radiobutton(self.myC2, text='만든 날짜별로 정리합니다.', variable=self.v0, value=1)
		self.R2.pack()
		self.R3 = tkinter.Radiobutton(self.myC2, text='수정한 날짜별로 정리합니다.', variable=self.v0, value=2)
		self.R3.pack()
		self.R4 = tkinter.Radiobutton(self.myC3, text='원래대로 되돌립니다.', variable=self.v0, value=9)
		self.R4.pack()
		self.C1 = tkinter.Checkbutton(self.myCy, text="정리한 후, 폴더 하나에 넣습니다.", variable=self.v1)
		self.C1.pack()
		self.B1 = tkinter.Button(self.myCx, text='적용')
		self.B1.pack(side=tkinter.LEFT)
		self.B1.bind("<Button-1>", self.B1Click)
		self.B2 = tkinter.Button(self.myCx, text='종료')
		self.B2.pack(side=tkinter.LEFT)
		self.B2.bind("<Button-1>", self.B2Click)
		self.n.add(self.myC1, text='확장자')
		self.n.add(self.myC2, text='시간')
		self.n.add(self.myC3, text='되돌리기')
	def B1Click(self, event):
		organize(self.v0.get(), self.v1.get())  # v 값에 따라 정리한다.
	def B2Click(self, event):
		self.myParent.destroy()  # 애플리케이션을 종료한다.
root = tkinter.Tk()
root.title("정리기")
root.minsize(200, 80)  # 애플리케이션의 최소 크기
myapp = MyApp(root)
root.mainloop()
