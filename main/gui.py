import sys
from PyQt5.QtWidgets import QApplication,QRadioButton,QStackedWidget, QListWidgetItem, QHBoxLayout, QLineEdit, QListWidget, QWidget, QVBoxLayout, QPushButton,QComboBox, QLabel
from PyQt5.QtCore import Qt, QSize
from dataFetcher import *
from confGen import*
class ResponsiveApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.setLayout(self.layout)
        self.verilogBtn = QPushButton("sirf verilog",self)
        self.projectBtn = QPushButton("pura project",self)
        self.combobox = QComboBox(self)
        self.showw = QLabel("Select some fpga to continue",self)
        self.showw.setStyleSheet("color:red")

        self.layout.addWidget(self.combobox)
        self.layout.addWidget(self.showw)
        self.layout.addWidget(self.verilogBtn)
        self.verilogBtn.setEnabled(False)
        self.verilogBtn.clicked.connect(self.onclick1)
        self.layout.addWidget(self.projectBtn)
        self.projectBtn.clicked.connect(self.onclick2)
        self.projectBtn.setEnabled(False)
        supported_fpgas=extractFPGAData()
        self.combobox.addItems(['Select']+supported_fpgas)
        self.combobox.currentIndexChanged.connect(self.choosinganother)  
        self.setStyleSheet("""
                                    QVBoxLayout{
                                        display:flex;
                                        border:solid;
                                        border-radius:20px;
                                        background-color:#F8FAFC;
                                        text-align:center;
                                        padding:20px;
                                    }
                                    QComboBox{
                                        border:solid;
                                        border-radius:20px;
                                        background-color:#2E5077;
                                        color:white;
                                        text-align:center;
                                        padding:20px;
                                        margin:10px;
                                        font-size:40px;
                                    }
                                    QLabel{
                                        border:2px solid black;
                                        border-radius:20px;
                                        background-color:#F5ECD5;
                                        color:black;
                                        font-size:40px;
                                        padding:20px;
                                        margin:40px;
                                        text-align:center;
                                    }
                                    QPushButton{
                                        border:solid;
                                        border-radius:20px;
                                        background-color:#578E7E;
                                        color:white;
                                        text-align:center;
                                        padding:20px;
                                        min-width: 10vw; 
                                        max-width: 10vw;
                                        font-size:40px;
                                    }
                                    QPushButton:hover{
                                        border:solid;
                                        border-radius:20px;
                                        background-color:black;
                                        color:white;
                                        text-align:center;
                                        padding:20px;
                                        font-size:40px;
                                        
                                        
                                    }
                                    """)
        

        self.setWindowTitle('Responsive PyQt5 App')

    def choosinganother(self, index):
        if index == 0:
            self.verilogBtn.setEnabled(False)
            self.projectBtn.setEnabled(False)
            self.showw.setText('Select some fpga to continue')
            self.showw.setStyleSheet("color:red")
        else:
            self.verilogBtn.setEnabled(True)
            self.projectBtn.setEnabled(True)
            global global_index 
            global_index= self.combobox.currentIndex()
            print(global_index)
            self.showw.setStyleSheet("color:black")
            self.deviceSelected= getFPGAInfo(self.combobox.currentText())
            self.showw.setText(f'FPGA: {self.combobox.currentText().upper()} \nFamily : {self.deviceSelected[0]} \nSoftware : {self.deviceSelected[1]} \nClock : {self.deviceSelected[2]}')

    
    def onclick1(self,index):
        wid.setCurrentIndex(wid.currentIndex() + 1)
        print(create_config([self.combobox.currentText(),self.deviceSelected[2],0]))
        print("Next Screen")        
        
    def onclick2(self,index):
        wid.setCurrentIndex(wid.currentIndex() + 1)
        print(create_config([self.combobox.currentText(),self.deviceSelected[2],1]))
        print("Next Screen")        
        
    
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        parent_width = self.width()
        new_button_width = int(parent_width * 0.4)
        self.verilogBtn.setFixedWidth(new_button_width)
        self.projectBtn.setFixedWidth(new_button_width)

    
class Screen2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('search bar')

        self.setStyleSheet("""
                                    QVBoxLayout{
                                        display:flex;
                                        border:solid;
                                        border-radius:20px;
                                        background-color:#F8FAFC;
                                        text-align:center;
                                        padding:20px;
                                    }
                                    QLabel{
                                        border:2px solid black;
                                        border-radius:20px;
                                        background-color:#F5ECD5;
                                        color:black;
                                        font-size:40px;
                                        padding:20px;
                                        margin:40px;
                                        text-align:center;
                                    }
                                    QLineEdit {
                                        background-color: #ffffff;  
                                        border: 1px solid #ccc;     
                                        border-radius: 5px;         
                                        padding: 8px 12px;         
                                        font-family: Arial, sans-serif;
                                        font-size: 50px;
                                    }

                                    QLineEdit:focus {
                                        border-color: #4CAF50;      
                                        background-color: #f9f9f9;  
                                    }

                                    QLineEdit::placeholder {
                                        color: #888;               
                                        font-style: italic;        
                                        font-size: 14px;
                                    }
                                    QListWidget {
                                        background-color: #f5f5f5; 
                                        border: 1px solid #ccc;     
                                        border-radius: 5px;         
                                        padding: 10px;
                                        font-size: 50px;
                                    }

                                    QListWidget::item {
                                        background-color: white;
                                        border: 1px solid transparent;
                                        padding: 10px;
                                        font-size: 50px;
                                        font-family: Arial, sans-serif;
                                    }

                                    QListWidget::item:hover {
                                        background-color: #e1e1e1;  
                                        cursor: pointer;
                                    }


                                    QListWidget::item:disabled {
                                        color: #ccc; /* Disabled text color */
                                    }
                                    QPushButton{
                                        border:solid;
                                        border-radius:20px;
                                        background-color:#578E7E;
                                        color:white;
                                        text-align:center;
                                        padding:20px;
                                        font-size:40px;
                                    }
                                    QPushButton:hover{
                                        border:solid;
                                        border-radius:20px;
                                        background-color:black;
                                        color:white;
                                        text-align:center;
                                        padding:20px;
                                        font-size:40px;
                                        
                                        
                                    }
                                    """)
        
        
        layout = QVBoxLayout()

        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.textChanged.connect(self.onChangeText)

        
        self.list_widget = QListWidget(self)
        self.listAdd()
        self.list_widget.clicked.connect(self.on_item_changed)

        self.selectedList = QListWidget(self)
        self.selectedList.setSelectionMode(QListWidget.NoSelection) 

        self.store_button = QPushButton("Store Selected Items", self)
        self.store_button.clicked.connect(self.store_selected_items)

        
        self.protocols=[]
        
        self.v_dabba=QVBoxLayout()
        self.sensorName = QLabel('here comes the name \n of the sensor',self)
        self.addBtn = QPushButton("add item", self)
        self.addBtn.clicked.connect(self.finalList)
        self.v_dabba.addWidget(self.sensorName)
        self.i2c = QRadioButton("I2C")
        self.uart = QRadioButton("UART")
        self.rs485 = QRadioButton("RS485")
        self.spi = QRadioButton("SPI")
        self.v_dabba.addWidget(self.i2c)
        self.v_dabba.addWidget(self.uart)
        self.v_dabba.addWidget(self.rs485)
        self.v_dabba.addWidget(self.spi)
        self.i2c.hide()
        self.uart.hide()
        self.rs485.hide()
        self.spi.hide()
        
        self.freq = QComboBox()
        self.v_dabba.addWidget(self.freq)
        self.freq.hide()
        
        self.i2c.toggled.connect(self.raidoi2c)
        self.uart.toggled.connect(self.raidouart)
        self.rs485.toggled.connect(self.raidors485) 
        self.spi.toggled.connect(self.raidospi)
        self.v_dabba.addWidget(self.addBtn)
        self.addBtn.setEnabled(False)
        h_dabba = QHBoxLayout()
        h_dabba.addWidget(self.list_widget)
        h_dabba.addLayout(self.v_dabba)
        h_dabba.addWidget(self.selectedList)
        
        


        layout.addWidget(self.search_bar)
        layout.addLayout(h_dabba)
        layout.addWidget(self.store_button)

        self.setLayout(layout)


    def raidouart(self):
        self.i2c.setChecked(False)
        self.rs485.setChecked(False)
        self.spi.setChecked(False)
        self.freq.clear()
        print('hello moto',self.txtt)
        self.freq.addItems(getProtocolDetails(self.txtt[0],'uart'))
    def raidoi2c(self):
        self.uart.setChecked(False)
        self.rs485.setChecked(False)
        self.spi.setChecked(False)
        self.freq.clear()
        self.freq.addItems(getProtocolDetails(self.txtt[0],'i2c'))
    def raidors485(self):
        self.i2c.setChecked(False)
        self.uart.setChecked(False)
        self.spi.setChecked(False)
        self.freq.clear()
        self.freq.addItems(getProtocolDetails(self.txtt[0],'RS485'))
    def raidospi(self):
        self.i2c.setChecked(False)
        self.rs485.setChecked(False)
        self.uart.setChecked(False)
        self.freq.clear()
        self.freq.addItems(getProtocolDetails(self.txtt[0],'spi'))
        
    
    def on_item_changed(self, index):
        self.i2c.setCheckable(False)
        self.uart.setCheckable(False)
        self.rs485.setCheckable(False)
        self.spi.setCheckable(False)
        self.txtt=[self.list_widget.item(index.row()).text()]
        self.addBtn.setEnabled(True)
        self.freq.show()
        # itm = QListWidgetItem(txtt)
        # self.selectedList.addItem(itm)
        self.protocols = getProtocols(self.list_widget.item(index.row()).text())
        self.sensorName.setText(f'sensor : {self.list_widget.item(index.row()).text()}')
        self.freq.clear()
        self.freq.addItems(getProtocolDetails(self.txtt[0],self.protocols[0]))
        self.i2c.hide()
        self.uart.hide()
        self.rs485.hide()
        self.spi.hide()
        self.i2c.setCheckable(True)
        self.uart.setCheckable(True)
        self.rs485.setCheckable(True)
        self.spi.setCheckable(True)
        for i in self.protocols:
            if(i=='i2c'):
                self.i2c.show()
            if(i=='uart'):
                self.uart.show()
            if(i=='RS485'):
                self.rs485.show()
            if(i=='spi'):
                self.spi.show()
        if(self.protocols[0]=='i2c'):
            self.i2c.setChecked(True)
            self.uart.setChecked(False)
            self.rs485.setChecked(False)
            self.spi.setChecked(False)
        if(self.protocols[0]=='uart'):
            self.uart.setChecked(True)
            self.i2c.setChecked(False)
            self.rs485.setChecked(False)
            self.spi.setChecked(False)
        if(self.protocols[0]=='RS485'):
            self.rs485.setChecked(True)
            self.uart.setChecked(False)
            self.i2c.setChecked(False)
            self.spi.setChecked(False)
        if(self.protocols[0]=='spi'):
            self.spi.setChecked(True)  
            self.uart.setChecked(False)
            self.i2c.setChecked(False)
            self.rs485.setChecked(False)
            
    def listAdd(self):
        items = getDevicesList()
        for item_text in items:
            item = QListWidgetItem(item_text)
            self.list_widget.addItem(item)

    def finalList(self):
        if(self.uart.isChecked()):self.txtt.append('uart')
        if(self.i2c.isChecked()):self.txtt.append('i2c')
        if(self.rs485.isChecked()):self.txtt.append('RS485')
        if(self.spi.isChecked()):self.txtt.append('spi')
        
        if(self.txtt[1]=="i2c"):
            self.txtt.append(addrFetcher(self.txtt[0]))
            self.txtt.append(self.freq.currentText())
            item = QListWidgetItem(f'{self.txtt[0]}\nprotocols: {self.txtt[1]}\naddress: {self.txtt[2]}\n{self.remo()}: {self.txtt[3]}Hz')   
        elif(self.txtt[1]=="uart"):
            self.txtt.append(self.freq.currentText())
            item = QListWidgetItem(f'{self.txtt[0]}\nprotocols: {self.txtt[1]}\n{self.remo()}: {self.txtt[2]}')
        else:
            self.txtt.append(self.freq.currentText())
            item = QListWidgetItem(f'{self.txtt[0]}\nprotocols: {self.txtt[1]}\n{self.remo()}: {self.txtt[2]}Hz')
        
        self.selectedList.addItem(item)
        print(self.txtt)
        add_sensors(self.txtt)
        
    def remo(self):
        if(self.txtt[1]=='uart'):
            return 'baud_rate'
        else:
            return 'frequency'
        
        
        
        
    def onChangeText(self):
        search_text = self.search_bar.text().lower()
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            item.setHidden(search_text not in item.text().lower())

    def store_selected_items(self):
        selected_items.clear()  
        for i in range(self.selectedList.count()):
            item = self.selectedList.item(i)
            selected_items.append(item.text())
        
        print("Selected items:", selected_items)
        wid.setCurrentIndex(wid.currentIndex() + 1)


class Screen3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('no. of items')

        self.setStyleSheet("""
                                    QVBoxLayout{
                                        display:flex;
                                        border:solid;
                                        border-radius:20px;
                                        background-color:#F8FAFC;
                                        text-align:center;
                                        padding:20px;
                                    }
                                    QLineEdit {
                                        background-color: #ffffff;  
                                        border: 1px solid #ccc;     
                                        border-radius: 5px;         
                                        padding: 8px 12px;         
                                        font-family: Arial, sans-serif;
                                        font-size: 50px;
                                    }

                                    QLineEdit:focus {
                                        border-color: #4CAF50;      
                                        background-color: #f9f9f9;  
                                    }

                                    QLineEdit::placeholder {
                                        color: #888;               
                                        font-style: italic;        
                                        font-size: 14px;
                                    }
                                    QListWidget {
                                        background-color: #f5f5f5; 
                                        border: 1px solid #ccc;     
                                        border-radius: 5px;         
                                        padding: 10px;
                                        font-size: 50px;
                                    }

                                    QListWidget::item {
                                        background-color: white;
                                        border: 1px solid transparent;
                                        padding: 10px;
                                        font-size: 50px;
                                        font-family: Arial, sans-serif;
                                    }

                                    QListWidget::item:hover {
                                        background-color: #e1e1e1;  
                                        cursor: pointer;
                                    }

                                    QListWidget::item:disabled {
                                        color: #ccc; /* Disabled text color */
                                    }
                                    QPushButton{
                                        border:solid;
                                        border-radius:20px;
                                        background-color:#578E7E;
                                        color:white;
                                        text-align:center;
                                        padding:20px;
                                        font-size:40px;
                                    }
                                    QPushButton:hover{
                                        border:solid;
                                        border-radius:20px;
                                        background-color:black;
                                        color:white;
                                        text-align:center;
                                        padding:20px;
                                        font-size:40px;
                                        
                                        
                                    }
                                    """)
        
        
        layout = QVBoxLayout()


        
        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QListWidget.NoSelection) 

        
        self.projectNaam = QLineEdit(self)
        self.projectNaam.setPlaceholderText("Search...")

        self.store_button = QPushButton("Ok, done", self)

        
        layout.addWidget(self.store_button)
        layout.addWidget(self.store_button)

        self.setLayout(layout)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid=QStackedWidget()
    selected_items = []
    mainwindow = ResponsiveApp()
    screen2 = Screen2()
    screen3 = Screen3()
    wid.addWidget(mainwindow)
    wid.addWidget(screen2)
    wid.addWidget(screen3)
    wid.show()
    mainwindow.show()
    wid.resize(1600, 1200)  # Initial size
    sys.exit(app.exec_())
