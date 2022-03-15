import sys 
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget,QLabel,QDesktopWidget,QMessageBox
from tkinter import messagebox
import os
import csv
lst = []
class UI(QDialog):     
    def __init__(self):
        super(UI,self).__init__()
        loadUi('stackedWindow.ui',self)
        self.id=['FFH01','FPP02','FCB03','FSW04']
        self.id1=['DCC01','DCC002','DM003','DWS04']
        self.pushButton_36.clicked.connect(self.eat)
        self.pushButton_48.clicked.connect(self.cart)
        self.pushButton_37.clicked.connect(self.drink)
        self.pushButton_40.clicked.connect(self.address)
        self.pushButton_41.clicked.connect(self.exit)
        self.pushButton_46.clicked.connect(self.home)
        self.pushButton_43.clicked.connect(self.drink)
        self.pushButton_45.clicked.connect(self.address)
        self.pushButton_68.clicked.connect(self.home)
        self.pushButton_66.clicked.connect(self.eat)
        self.pushButton_67.clicked.connect(self.address)
        self.pushButton_72.clicked.connect(self.home)
        self.pushButton_70.clicked.connect(self.eat)
        self.pushButton_69.clicked.connect(self.drink)
        self.pushButton_47.clicked.connect(self.cart)
        self.pushButton_79.clicked.connect(self.cart)
        self.pushButton_78.clicked.connect(self.cart)
        self.pushButton_76.clicked.connect(self.home)
        self.pushButton_74.clicked.connect(self.eat)
        self.pushButton_73.clicked.connect(self.drink)
        self.pushButton_75.clicked.connect(self.address)
        self.pushButton_18.clicked.connect(self.rate)
        self.pushButton_19.clicked.connect(self.rate1)
        self.pushButton_20.clicked.connect(self.rate2)
        self.pushButton_38.clicked.connect(self.rate3)
        self.pushButton_28.clicked.connect(self.d1)
        self.pushButton_26.clicked.connect(self.d2)
        self.pushButton_29.clicked.connect(self.d3)
        self.pushButton_27.clicked.connect(self.d4)
        self.pushButton_42.clicked.connect(self.special)
        self.pushButton_21.clicked.connect(self.order)
        self.pushButton_30.clicked.connect(self.submit)
        
#-----------------------------------------------------------Methods-----------------------------------------------------------------------
    def submit(self):
        if self.lineEdit.text()=='' and self.lineEdit_3.text()=='' and self.textEdit.toPlainText()=='':
            messagebox.showerror('Error','All Fiels Required')
        else:
            messagebox.showinfo('Cherri','Succesfully Sumbmited')
            
    def order(self):
        if self.lineEdit_2.text()=='' and self.lineEdit.text()=='' and self.lineEdit_3.text()=='' and self.textEdit.toPlainText()=='':
            messagebox.showerror('Error','Please Enter Customer Name and Address')
        else:
            a=self.lineEdit_2.text()!='' and self.lineEdit.text()!='' and self.lineEdit_3.text()!='' and self.textEdit.toPlainText()!=''
            if a==True:
                messagebox.showinfo('Cherri','Order Done Succesfully')
                with open(f'Bill/{self.lineEdit_2.text()}.csv','a',newline='') as f:
                    writer = csv.writer(f)
                    Customer = self.lineEdit_2.text()
                    CntNum = self.lineEdit.text()
                    HN = self.lineEdit_3.text()
                    Loc = self.textEdit.toPlainText()
                    csvwriter = csv.writer(f)
                    csvwriter.writerow(['Customer Name','Contanct Number','House Number','Address'])
                    csvwriter.writerow([Customer,CntNum,HN,Loc])
                    csvwriter.writerow([])
                    csvwriter.writerow([])
                    csvwriter.writerow([])
                    #csvwriter.writerow([])
                    #csvwriter.writerow([])
                    csvwriter.writerow(['Item','Quantity','Rate'])
                    csvwriter.writerow([self.lineEdit_18.text(),self.lineEdit_54.text(),self.lineEdit_54.text()])
                    csvwriter.writerow([self.lineEdit_20.text(),self.lineEdit_57.text(),self.lineEdit_25.text()])
                    csvwriter.writerow([self.lineEdit_29.text(),self.lineEdit_19.text(),self.lineEdit_58.text()])
                    csvwriter.writerow([self.lineEdit_31.text(),self.lineEdit_52.text(),self.lineEdit_26.text()])
                    csvwriter.writerow([self.lineEdit_32.text(),self.lineEdit_47.text(),self.lineEdit_21.text()])
                    csvwriter.writerow([self.lineEdit_17.text(),self.lineEdit_55.text(),self.lineEdit_22.text()])
                    csvwriter.writerow([self.lineEdit_27.text(),self.lineEdit_60.text(),self.lineEdit_23.text()])
                  
                    self.lineEdit_2.clear()
                    self.lineEdit_56.clear()
                    self.lineEdit_54.clear()
                    self.lineEdit_30.clear()
                    self.lineEdit_18.clear()
                    self.lineEdit_49.clear()
                    self.lineEdit_57.clear()
                    self.lineEdit_25.clear()
                    self.lineEdit_20.clear()
                    self.lineEdit_53.clear()
                    self.lineEdit_58.clear()
                    self.lineEdit_19.clear()
                    self.lineEdit_29.clear()
                    self.lineEdit_59.clear()
                    self.lineEdit_52.clear()
                    self.lineEdit_26.clear()
                    self.lineEdit_31.clear()
                    self.lineEdit_48.clear()
                    self.lineEdit_47.clear()
                    self.lineEdit_21.clear()
                    self.lineEdit_32.clear()
                    self.lineEdit_62.clear()
                    self.lineEdit_55.clear()
                    self.lineEdit_22.clear()
                    self.lineEdit_17.clear()
                    self.lineEdit_61.clear()
                    self.lineEdit_60.clear()
                    self.lineEdit_23.clear()
                    self.lineEdit_27.clear()
                    self.lineEdit_50.clear()
                    self.doubleSpinBox_3.setValue(0.00)
                    self.doubleSpinBox_4.setValue(0.00)
                    self.doubleSpinBox.setValue(0.00)
                    self.doubleSpinBox_16.setValue(0.00)
                    self.doubleSpinBox_9.setValue(0.00)
                    self.doubleSpinBox_2.setValue(0.00)
                    self.doubleSpinBox_5.setValue(0.00)
                    self.doubleSpinBox_17.setValue(0.00)
                    self.doubleSpinBox_10.setValue(0.00)                
                f.close()
            else:
                messagebox.showerror('Error','Please Enter Customer Name and Address')

    def special(self):
        if self.lineEdit_18.text()=='' or self.lineEdit_18.text()=='Special Veggie Supreme':               
            self.qty = int(self.doubleSpinBox_3.value())
            self.Rate =589*self.qty 
            self.lineEdit_56.setText('SPSVS1')
            self.lineEdit_54.setText(str(self.qty))
            self.lineEdit_30.setText(str(self.Rate))
            self.lineEdit_18.setText('Special Veggie Supreme')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_20.text()=='' or self.lineEdit_20.text()=='Special Veggie Supreme':
            self.qty = int(self.doubleSpinBox_3.value())
            self.Rate =589*self.qty
            self.lineEdit_49.setText('SPSVS1')
            self.lineEdit_57.setText(str(self.qty))
            self.lineEdit_25.setText(str(self.Rate))
            self.lineEdit_20.setText('Special Veggie Supreme')  
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))   
        elif self.lineEdit_29.text()=='' or self.lineEdit_20.text()=='Special Veggie Supreme':
            self.qty = int(self.doubleSpinBox_3.value())
            self.Rate =589*self.qty          
            self.lineEdit_53.setText('SPSVS1')
            self.lineEdit_58.setText(str(self.qty))
            self.lineEdit_19.setText(str(self.Rate))
            self.lineEdit_29.setText('Special Veggie Supreme')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_31.text()=='' or self.lineEdit_20.text()=='Special Veggie Supreme':
            self.qty = int(self.doubleSpinBox_3.value())
            self.Rate =589*self.qty         
            self.lineEdit_59.setText('SPSVS1')
            self.lineEdit_52.setText(str(self.qty))
            self.lineEdit_26.setText(str(self.Rate))
            self.lineEdit_31.setText('Special Veggie Supreme')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_32.text()=='' or self.lineEdit_20.text()=='Special Veggie Supreme':
            self.qty = int(self.doubleSpinBox_3.value())
            self.Rate =589*self.qty         
            self.lineEdit_48.setText('SPSVS1')
            self.lineEdit_47.setText(str(self.qty))
            self.lineEdit_21.setText(str(self.Rate))
            self.lineEdit_32.setText('Special Veggie Supreme')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_17.text()=='' or self.lineEdit_20.text()=='Special Veggie Supreme':
            self.qty = int(self.doubleSpinBox_3.value())
            self.Rate =589*self.qty        
            self.lineEdit_62.setText('SPSVS1')
            self.lineEdit_55.setText(str(self.qty))
            self.lineEdit_22.setText(str(self.Rate))
            self.lineEdit_17.setText('Special Veggie Supreme')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst))) 
        else :
            self.qty = int(self.doubleSpinBox_3.value())
            self.Rate =589*self.qty
            self.lineEdit_61.setText('SPSVS1')
            self.lineEdit_60.setText(str(self.qty))
            self.lineEdit_23.setText(str(self.Rate))
            self.lineEdit_27.setText('Special Veggie Supreme')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
       
    
    def rate(self):
        if self.lineEdit_18.text()=='' or self.lineEdit_18.text()=='FARM HOUSE':
            self.qty = int(self.doubleSpinBox.value())
            self.Rate =584*self.qty 
            self.lineEdit_56.setText(str(self.id[0]))
            self.lineEdit_54.setText(str(self.qty))
            self.lineEdit_30.setText(str(self.Rate))
            self.lineEdit_18.setText('FARM HOUSE')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_20.text()=='' or self.lineEdit_20.text()=='FARM HOUSE':
            self.qty = int(self.doubleSpinBox.value())
            self.Rate =584*self.qty 
            self.lineEdit_49.setText(str(self.id[0]))
            self.lineEdit_57.setText(str(self.qty))
            self.lineEdit_25.setText(str(self.Rate))
            self.lineEdit_20.setText('FARM HOUSE')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
              
        elif self.lineEdit_29.text()=='' or self.lineEdit_20.text()=='FARM HOUSE':
            self.qty = int(self.doubleSpinBox.value())
            self.Rate =584*self.qty 
            self.lineEdit_53.setText(str(self.id[0]))
            self.lineEdit_58.setText(str(self.qty))
            self.lineEdit_19.setText(str(self.Rate))
            self.lineEdit_29.setText('FARM HOUSE')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_31.text()=='' or self.lineEdit_20.text()=='FARM HOUSE':
            self.qty = int(self.doubleSpinBox.value())
            self.Rate =584*self.qty 
            self.lineEdit_59.setText(str(self.id[0]))
            self.lineEdit_52.setText(str(self.qty))
            self.lineEdit_26.setText(str(self.Rate))
            self.lineEdit_31.setText('FARM HOUSE')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_32.text()=='' or self.lineEdit_20.text()=='FARM HOUSE':
            self.qty = int(self.doubleSpinBox.value())
            self.Rate =584*self.qty 
            self.lineEdit_56.setText(str(self.id[0]))
            self.lineEdit_47.setText(str(self.qty))
            self.lineEdit_21.setText(str(self.Rate))
            self.lineEdit_31.setText('FARM HOUSE')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_17.text()=='' or self.lineEdit_20.text()=='FARM HOUSE':
            self.qty = int(self.doubleSpinBox.value())
            self.Rate =584*self.qty 
            self.lineEdit_62.setText(str(self.id[0]))
            self.lineEdit_55.setText(str(self.qty))
            self.lineEdit_22.setText(str(self.Rate))
            self.lineEdit_17.setText('FARM HOUSE')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst))) 
        else :
            self.qty = int(self.doubleSpinBox.value())
            self.Rate =584*self.qty
            self.lineEdit_61.setText(str(self.id[0]))
            self.lineEdit_60.setText(str(self.qty))
            self.lineEdit_23.setText(str(self.Rate))
            self.lineEdit_27.setText('FARM HOUSE')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        
    
    def rate1(self):
        if self.lineEdit_18.text()=='' or self.lineEdit_18.text()=='PEPPY PANEER':
            self.qty = int(self.doubleSpinBox_4.value())
            self.Rate =384*self.qty 
            self.lineEdit_56.setText(str(self.id[1]))
            self.lineEdit_54.setText(str(self.qty))
            self.lineEdit_30.setText(str(self.Rate))
            self.lineEdit_18.setText('PEPPY PANEER')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_20.text()=='' or self.lineEdit_20.text()=='PEPPY PANEER':
            self.qty = int(self.doubleSpinBox_4.value())
            self.Rate =384*self.qty 
            self.lineEdit_49.setText(str(self.id[1]))
            self.lineEdit_57.setText(str(self.qty))
            self.lineEdit_25.setText(str(self.Rate))
            self.lineEdit_20.setText('PEPPY PANEER')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))     
        elif self.lineEdit_29.text()=='' or self.lineEdit_20.text()=='PEPPY PANEER':
            self.qty = int(self.doubleSpinBox_4.value())
            self.Rate =384*self.qty            
            self.lineEdit_53.setText(str(self.id[1]))
            self.lineEdit_58.setText(str(self.qty))
            self.lineEdit_19.setText(str(self.Rate))
            self.lineEdit_29.setText('PEPPY PANEER')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_31.text()=='' or self.lineEdit_20.text()=='PEPPY PANEER':
            self.qty = int(self.doubleSpinBox_4.value())
            self.Rate =384*self.qty            
            self.lineEdit_59.setText(str(self.id[1]))
            self.lineEdit_52.setText(str(self.qty))
            self.lineEdit_26.setText(str(self.Rate))
            self.lineEdit_31.setText('PEPPY PANEER')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_32.text()=='' or self.lineEdit_20.text()=='PEPPY PANEER':
            self.qty = int(self.doubleSpinBox_4.value())
            self.Rate =384*self.qty            
            self.lineEdit_56.setText(str(self.id[1]))
            self.lineEdit_47.setText(str(self.qty))
            self.lineEdit_21.setText(str(self.Rate))
            self.lineEdit_31.setText('PEPPY PANEER')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_17.text()=='' or self.lineEdit_20.text()=='PEPPY PANEER':
            self.qty = int(self.doubleSpinBox_4.value())
            self.Rate =384*self.qty             
            self.lineEdit_62.setText(str(self.id[1]))
            self.lineEdit_55.setText(str(self.qty))
            self.lineEdit_22.setText(str(self.Rate))
            self.lineEdit_17.setText('PEPPY PANEER')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst))) 
        else :
            self.qty = int(self.doubleSpinBox_4.value())
            self.Rate =384*self.qty
            self.lineEdit_61.setText(str(self.id[1]))
            self.lineEdit_60.setText(str(self.qty))
            self.lineEdit_23.setText(str(self.Rate))
            self.lineEdit_27.setText('PEPPY PANEER')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
    
     
    def rate2(self):
        if self.lineEdit_18.text()=='' or self.lineEdit_18.text()=='Chilli Burger':
            self.qty = int(self.doubleSpinBox_16.value())
            self.Rate =142*self.qty 
            self.lineEdit_56.setText(str(self.id[2]))
            self.lineEdit_54.setText(str(self.qty))
            self.lineEdit_30.setText(str(self.Rate))
            self.lineEdit_18.setText('Chilli Burger')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_20.text()=='' or self.lineEdit_18.text()=='Chilli Burger':
            self.qty = int(self.doubleSpinBox_16.value())
            self.Rate =142*self.qty  
            self.lineEdit_49.setText(str(self.id[2]))
            self.lineEdit_57.setText(str(self.qty))
            self.lineEdit_25.setText(str(self.Rate))
            self.lineEdit_20.setText('Chilli Burger') 
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))    
        elif self.lineEdit_29.text()=='' or self.lineEdit_18.text()=='Chilli Burger':
            self.qty = int(self.doubleSpinBox_16.value())
            self.Rate =142*self.qty  
            self.lineEdit_53.setText(str(self.id[2]))
            self.lineEdit_58.setText(str(self.qty))
            self.lineEdit_19.setText(str(self.Rate))
            self.lineEdit_29.setText('Chilli Burger')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_31.text()=='' or self.lineEdit_18.text()=='Chilli Burger':
            self.qty = int(self.doubleSpinBox_16.value())
            self.Rate =142*self.qty  
            self.lineEdit_59.setText(str(self.id[2]))
            self.lineEdit_52.setText(str(self.qty))
            self.lineEdit_26.setText(str(self.Rate))
            self.lineEdit_31.setText('Chilli Burger')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_32.text()=='' or self.lineEdit_18.text()=='Chilli Burger':
            self.qty = int(self.doubleSpinBox_16.value())
            self.Rate =142*self.qty  
            self.lineEdit_56.setText(str(self.id[2]))
            self.lineEdit_47.setText(str(self.qty))
            self.lineEdit_21.setText(str(self.Rate))
            self.lineEdit_31.setText('Chilli Burger')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_17.text()=='' or self.lineEdit_18.text()=='Chilli Burger':
            self.qty = int(self.doubleSpinBox_16.value())
            self.Rate =142*self.qty  
            self.lineEdit_62.setText(str(self.id[2]))
            self.lineEdit_55.setText(str(self.qty))
            self.lineEdit_22.setText(str(self.Rate))
            self.lineEdit_17.setText('Chilli Burger') 
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        else :
            self.qty = int(self.doubleSpinBox_16.value())
            self.Rate =142*self.qty 
            self.lineEdit_61.setText(str(self.id[2]))
            self.lineEdit_60.setText(str(self.qty))
            self.lineEdit_23.setText(str(self.Rate))
            self.lineEdit_27.setText('Chilli Burger')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
  
        
    def rate3(self):
        if self.lineEdit_18.text()=='' or self.lineEdit_18.text()=='Sweet Corn':
            self.qty = int(self.doubleSpinBox_9.value())
            self.Rate =89*self.qty 
            self.lineEdit_56.setText(str(self.id[3]))
            self.lineEdit_54.setText(str(self.qty))
            self.lineEdit_30.setText(str(self.Rate))
            self.lineEdit_18.setText('Sweet Corn')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_20.text()=='' or self.lineEdit_18.text()=='Sweet Corn':
            self.qty = int(self.doubleSpinBox_9.value())
            self.Rate =89*self.qty 
            self.lineEdit_49.setText(str(self.id[3]))
            self.lineEdit_57.setText(str(self.qty))
            self.lineEdit_25.setText(str(self.Rate))
            self.lineEdit_20.setText('Sweet Corn')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
              
        elif self.lineEdit_29.text()=='' or self.lineEdit_18.text()=='Sweet Corn':
            self.qty = int(self.doubleSpinBox_9.value())
            self.Rate =89*self.qty 
            self.lineEdit_53.setText(str(self.id[3]))
            self.lineEdit_58.setText(str(self.qty))
            self.lineEdit_19.setText(str(self.Rate))
            self.lineEdit_29.setText('Sweet Corn')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_31.text()=='' or self.lineEdit_18.text()=='Sweet Corn':
            self.qty = int(self.doubleSpinBox_9.value())
            self.Rate =89*self.qty 
            self.lineEdit_59.setText(str(self.id[3]))
            self.lineEdit_52.setText(str(self.qty))
            self.lineEdit_26.setText(str(self.Rate))
            self.lineEdit_31.setText('Sweet Corn')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_32.text()=='' or self.lineEdit_18.text()=='Sweet Corn':
            self.qty = int(self.doubleSpinBox_9.value())
            self.Rate =89*self.qty 
            self.lineEdit_56.setText(str(self.id[3]))
            self.lineEdit_47.setText(str(self.qty))
            self.lineEdit_21.setText(str(self.Rate))
            self.lineEdit_31.setText('Sweet Corn')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_17.text()=='' or self.lineEdit_18.text()=='Sweet Corn':
            self.qty = int(self.doubleSpinBox_9.value())
            self.Rate =89*self.qty 
            self.lineEdit_62.setText(str(self.id[3]))
            self.lineEdit_55.setText(str(self.qty))
            self.lineEdit_22.setText(str(self.Rate))
            self.lineEdit_17.setText('Sweet Corn') 
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        else :
            self.qty = int(self.doubleSpinBox_9.value())
            self.Rate =89*self.qty
            self.lineEdit_61.setText(str(self.id[3]))
            self.lineEdit_60.setText(str(self.qty))
            self.lineEdit_23.setText(str(self.Rate))
            self.lineEdit_27.setText('Sweet Corn')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
     

    def d1(self):
        if self.lineEdit_18.text()=='' or self.lineEdit_18.text()=='Coco-Cola':
            self.qty = int(self.doubleSpinBox_2.value())
            self.Rate =54*self.qty 
            self.lineEdit_56.setText(str(self.id1[0]))
            self.lineEdit_54.setText(str(self.qty))
            self.lineEdit_30.setText(str(self.Rate))
            self.lineEdit_18.setText('Coco-Cola')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_20.text()=='' or self.lineEdit_20.text()=='Coco-Cola':
            self.qty = int(self.doubleSpinBox_2.value())
            self.Rate =54*self.qty 
            self.lineEdit_49.setText(str(self.id1[0]))
            self.lineEdit_57.setText(str(self.qty))
            self.lineEdit_25.setText(str(self.Rate))
            self.lineEdit_20.setText('Coco-Cola')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
              
        elif self.lineEdit_29.text()=='' or self.lineEdit_20.text()=='Coco-Cola':
            self.qty = int(self.doubleSpinBox_2.value())
            self.Rate =54*self.qty
            self.lineEdit_53.setText(str(self.id1[0]))
            self.lineEdit_58.setText(str(self.qty))
            self.lineEdit_19.setText(str(self.Rate))
            self.lineEdit_29.setText('Coco-Cola')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_31.text()=='' or self.lineEdit_20.text()=='Coco-Cola':
            self.qty = int(self.doubleSpinBox_2.value())
            self.Rate =54*self.qty 
            self.lineEdit_59.setText(str(self.id1[0]))
            self.lineEdit_52.setText(str(self.qty))
            self.lineEdit_26.setText(str(self.Rate))
            self.lineEdit_31.setText('Coco-Cola')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_32.text()=='' or self.lineEdit_20.text()=='Coco-Cola':
            self.qty = int(self.doubleSpinBox_2.value())
            self.Rate =54*self.qty 
            self.lineEdit_56.setText(str(self.id1[0]))
            self.lineEdit_47.setText(str(self.qty))
            self.lineEdit_21.setText(str(self.Rate))
            self.lineEdit_31.setText('Coco-Cola')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_17.text()=='' or self.lineEdit_20.text()=='Coco-Cola':
            self.qty = int(self.doubleSpinBox_2.value())
            self.Rate =54*self.qty 
            self.lineEdit_62.setText(str(self.id1[0]))
            self.lineEdit_55.setText(str(self.qty))
            self.lineEdit_22.setText(str(self.Rate))
            self.lineEdit_17.setText('Coco-Cola') 
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        else :
            self.qty = int(self.doubleSpinBox_2.value())
            self.Rate =54*self.qty
            self.lineEdit_61.setText(str(self.id1[0]))
            self.lineEdit_60.setText(str(self.qty))
            self.lineEdit_23.setText(str(self.Rate))
            self.lineEdit_27.setText('Coco-Cola')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
    

    def d2(self):
        if self.lineEdit_18.text()=='' or self.lineEdit_18.text()=='Cosmopolitan':
            self.qty = int(self.doubleSpinBox_5.value())
            self.Rate =178*self.qty 
            self.lineEdit_56.setText(str(self.id1[1]))
            self.lineEdit_54.setText(str(self.qty))
            self.lineEdit_30.setText(str(self.Rate))
            self.lineEdit_18.setText('Cosmopolitan')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_20.text()=='' or self.lineEdit_20.text()=='Cosmopolitan':
            self.qty = int(self.doubleSpinBox_5.value())
            self.Rate =178*self.qty 
            self.lineEdit_49.setText(str(self.id1[1]))
            self.lineEdit_57.setText(str(self.qty))
            self.lineEdit_25.setText(str(self.Rate))
            self.lineEdit_20.setText('Cosmopolitan')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))     
        elif self.lineEdit_29.text()=='' or self.lineEdit_20.text()=='Cosmopolitan':
            self.qty = int(self.doubleSpinBox_5.value())
            self.Rate =178*self.qty            
            self.lineEdit_53.setText(str(self.id1[1]))
            self.lineEdit_58.setText(str(self.qty))
            self.lineEdit_19.setText(str(self.Rate))
            self.lineEdit_29.setText('Cosmopolitan')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_31.text()=='' or self.lineEdit_20.text()=='Cosmopolitan':
            self.qty = int(self.doubleSpinBox_5.value())
            self.Rate =178*self.qty            
            self.lineEdit_59.setText(str(self.id1[1]))
            self.lineEdit_52.setText(str(self.qty))
            self.lineEdit_26.setText(str(self.Rate))
            self.lineEdit_31.setText('Cosmopolitan')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_32.text()=='' or self.lineEdit_20.text()=='Cosmopolitan':
            self.qty = int(self.doubleSpinBox_5.value())
            self.Rate =178*self.qty            
            self.lineEdit_48.setText(str(self.id1[1]))
            self.lineEdit_47.setText(str(self.qty))
            self.lineEdit_21.setText(str(self.Rate))
            self.lineEdit_32.setText('Cosmopolitan')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_17.text()=='' or self.lineEdit_20.text()=='Cosmopolitan':
            self.qty = int(self.doubleSpinBox_5.value())
            self.Rate =178*self.qty             
            self.lineEdit_62.setText(str(self.id1[1]))
            self.lineEdit_55.setText(str(self.qty))
            self.lineEdit_22.setText(str(self.Rate))
            self.lineEdit_17.setText('Cosmopolitan') 
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        else :
            self.qty = int(self.doubleSpinBox_5.value())
            self.Rate =178*self.qty
            self.lineEdit_61.setText(str(self.id1[1]))
            self.lineEdit_60.setText(str(self.qty))
            self.lineEdit_23.setText(str(self.Rate))
            self.lineEdit_27.setText('Cosmopolitan')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
  
    def d3(self):
        if self.lineEdit_18.text()=='' or self.lineEdit_18.text()=='Martini':
            self.qty = int(self.doubleSpinBox_17.value())
            self.Rate =98*self.qty 
            self.lineEdit_56.setText(str(self.id1[2]))
            self.lineEdit_54.setText(str(self.qty))
            self.lineEdit_30.setText(str(self.Rate))
            self.lineEdit_18.setText('Martini')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_20.text()=='' or self.lineEdit_20.text()=='Martini':
            self.qty = int(self.doubleSpinBox_17.value())
            self.Rate =98*self.qty 
            self.lineEdit_49.setText(str(self.id1[2]))
            self.lineEdit_57.setText(str(self.qty))
            self.lineEdit_25.setText(str(self.Rate))
            self.lineEdit_20.setText('Martini')     
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_29.text()=='' or self.lineEdit_20.text()=='Martini':
            self.qty = int(self.doubleSpinBox_17.value())
            self.Rate =98*self.qty            
            self.lineEdit_53.setText(str(self.id1[2]))
            self.lineEdit_58.setText(str(self.qty))
            self.lineEdit_19.setText(str(self.Rate))
            self.lineEdit_29.setText('Martini')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_31.text()=='' or self.lineEdit_20.text()=='Martini':
            self.qty = int(self.doubleSpinBox_17.value())
            self.Rate =98*self.qty            
            self.lineEdit_59.setText(str(self.id1[2]))
            self.lineEdit_52.setText(str(self.qty))
            self.lineEdit_26.setText(str(self.Rate))
            self.lineEdit_31.setText('Martini')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_32.text()=='' or self.lineEdit_20.text()=='Martini':
            self.qty = int(self.doubleSpinBox_17.value())
            self.Rate =98*self.qty            
            self.lineEdit_48.setText(str(self.id1[2]))
            self.lineEdit_47.setText(str(self.qty))
            self.lineEdit_21.setText(str(self.Rate))
            self.lineEdit_32.setText('Martini')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_17.text()=='' or self.lineEdit_20.text()=='Martini':
            self.qty = int(self.doubleSpinBox_17.value())
            self.Rate =98*self.qty             
            self.lineEdit_62.setText(str(self.id1[2]))
            self.lineEdit_55.setText(str(self.qty))
            self.lineEdit_22.setText(str(self.Rate))
            self.lineEdit_17.setText('Martini') 
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        else :
            self.qty = int(self.doubleSpinBox_17.value())
            self.Rate =98*self.qty
            self.lineEdit_61.setText(str(self.id1[2]))
            self.lineEdit_60.setText(str(self.qty))
            self.lineEdit_23.setText(str(self.Rate))
            self.lineEdit_27.setText('Martini')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))

        
    def d4(self):
        if self.lineEdit_18.text()=='' or self.lineEdit_18.text()=='Whiskey Sour':
            self.qty = int(self.doubleSpinBox_10.value())
            self.Rate =69*self.qty 
            self.lineEdit_56.setText(str(self.id1[3]))
            self.lineEdit_54.setText(str(self.qty))
            self.lineEdit_30.setText(str(self.Rate))
            self.lineEdit_18.setText('Whiskey Sour')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_20.text()=='' or self.lineEdit_20.text()=='Whiskey Sour':
            self.qty = int(self.doubleSpinBox_10.value())
            self.Rate =69*self.qty 
            self.lineEdit_49.setText(str(self.id1[3]))
            self.lineEdit_57.setText(str(self.qty))
            self.lineEdit_25.setText(str(self.Rate))
            self.lineEdit_20.setText('Whiskey Sour')  
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))   
        elif self.lineEdit_29.text()=='' or self.lineEdit_20.text()=='Whiskey Sour':
            self.qty = int(self.doubleSpinBox_10.value())
            self.Rate =69*self.qty           
            self.lineEdit_53.setText(str(self.id1[3]))
            self.lineEdit_58.setText(str(self.qty))
            self.lineEdit_19.setText(str(self.Rate))
            self.lineEdit_29.setText('Whiskey Sour')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_31.text()=='' or self.lineEdit_20.text()=='Whiskey Sour':
            self.qty = int(self.doubleSpinBox_10.value())
            self.Rate =69*self.qty          
            self.lineEdit_59.setText(str(self.id1[3]))
            self.lineEdit_52.setText(str(self.qty))
            self.lineEdit_26.setText(str(self.Rate))
            self.lineEdit_31.setText('Whiskey Sour')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_32.text()=='' or self.lineEdit_20.text()=='Whiskey Sour':
            self.qty = int(self.doubleSpinBox_10.value())
            self.Rate =69*self.qty           
            self.lineEdit_48.setText(str(self.id1[3]))
            self.lineEdit_47.setText(str(self.qty))
            self.lineEdit_21.setText(str(self.Rate))
            self.lineEdit_32.setText('Whiskey Sour')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))
        elif self.lineEdit_17.text()=='' or self.lineEdit_20.text()=='Whiskey Sour':
            self.qty = int(self.doubleSpinBox_10.value())
            self.Rate =69*self.qty            
            self.lineEdit_62.setText(str(self.id1[3]))
            self.lineEdit_55.setText(str(self.qty))
            self.lineEdit_22.setText(str(self.Rate))
            self.lineEdit_17.setText('Whiskey Sour')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst))) 
        else :
            self.qty = int(self.doubleSpinBox_10.value())
            self.Rate =69*self.qty
            self.lineEdit_61.setText(str(self.id1[3]))
            self.lineEdit_60.setText(str(self.qty))
            self.lineEdit_23.setText(str(self.Rate))
            self.lineEdit_27.setText('Whiskey Sour')
            lst.append(self.Rate)
            self.lineEdit_50.setText(str(sum(lst)))

    def eat(self):
        self.stackedWidget.setCurrentWidget(self.Food) 
    def drink(self):
        self.stackedWidget.setCurrentWidget(self.Drink)
    def address(self):
        self.stackedWidget.setCurrentWidget(self.Address)
    def exit(self):
        sys.exit()
    def home(self):
        self.stackedWidget.setCurrentWidget(self.Home)
    def cart(self):
        self.stackedWidget.setCurrentWidget(self.Bill)

app = QApplication(sys.argv)
welcome = UI()
welcome.setWindowTitle('Cherri')
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setWindowTitle('C H E R R I')
widget.setFixedHeight(650)
widget.setFixedWidth(900)
widget.move(250,20)
widget.show()
sys.exit(app.exec_())
