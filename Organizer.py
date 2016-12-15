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
			if os.path.isfile(i) == True:  # ������ ��� Ȯ���ں��� �з��� �����Ѵ�.
				if os.path.splitext(i)[1] != '':  # Ȯ���ڰ� ���� ���� ���� ������ ����� �����Ѵ�.
					os.renames(i, os.path.abspath(os.path.splitext(i)[1] + '\\' + i))
				else:
					os.renames(i, os.path.abspath('Ȯ���� ����\\' + i))
			else:
					os.renames(i, os.path.abspath("����\\" + i))
		elif x == 1:
			os.renames(i, os.path.abspath(datetime.datetime.fromtimestamp(float(os.stat(i)[7])).strftime('%Y-%m-%d') + '\\' + i))  # ���� ��¥���� �����Ѵ�.
		elif x == 2:
			os.renames(i, os.path.abspath(datetime.datetime.fromtimestamp(float(os.stat(i)[8])).strftime('%Y-%m-%d') + '\\' + i))  # ������ ��¥���� �����Ѵ�.
		elif x == 9:
			y = False
			for i in os.listdir():  # ������� �ǵ�����.
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
		self.myC1 = tkinter.Frame(self.n)  # Ȯ���ں��� �����ϴ� ���� ��ư�� �� ������.
		self.myC1.pack()
		self.myC2 = tkinter.Frame(self.n)  # �ð����� �����ϴ� ���� ��ư�� �� ������.
		self.myC2.pack()
		self.myC3 = tkinter.Frame(self.n)  # ������ ������ ������� �ǵ��� ���� ��ư�� �� ������.
		self.myC3.pack()
		self.myCy = tkinter.Frame(parent)
		self.myCy.pack()
		self.myCx = tkinter.Frame(parent)  # ��ư�� �� ������.
		self.myCx.pack()
		self.R1 = tkinter.Radiobutton(self.myC1, text='Ȯ���ں��� �����մϴ�.', variable=self.v0, value=0)
		self.R1.pack()
		self.R2 = tkinter.Radiobutton(self.myC2, text='���� ��¥���� �����մϴ�.', variable=self.v0, value=1)
		self.R2.pack()
		self.R3 = tkinter.Radiobutton(self.myC2, text='������ ��¥���� �����մϴ�.', variable=self.v0, value=2)
		self.R3.pack()
		self.R4 = tkinter.Radiobutton(self.myC3, text='������� �ǵ����ϴ�.', variable=self.v0, value=9)
		self.R4.pack()
		self.C1 = tkinter.Checkbutton(self.myCy, text="������ ��, ���� �ϳ��� �ֽ��ϴ�.", variable=self.v1)
		self.C1.pack()
		self.B1 = tkinter.Button(self.myCx, text='����')
		self.B1.pack(side=tkinter.LEFT)
		self.B1.bind("<Button-1>", self.B1Click)
		self.B2 = tkinter.Button(self.myCx, text='����')
		self.B2.pack(side=tkinter.LEFT)
		self.B2.bind("<Button-1>", self.B2Click)
		self.n.add(self.myC1, text='Ȯ����')
		self.n.add(self.myC2, text='�ð�')
		self.n.add(self.myC3, text='�ǵ�����')
	def B1Click(self, event):
		organize(self.v0.get(), self.v1.get())  # v ���� ���� �����Ѵ�.
	def B2Click(self, event):
		self.myParent.destroy()  # ���ø����̼��� �����Ѵ�.
root = tkinter.Tk()
root.title("������")
root.minsize(200, 80)  # ���ø����̼��� �ּ� ũ��
myapp = MyApp(root)
root.mainloop()
