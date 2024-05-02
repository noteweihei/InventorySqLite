from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox,QPushButton,QLabel,QLineEdit, QWidget,QVBoxLayout,QTableWidget,QTableWidgetItem,QHBoxLayout
import sys
import sqlite3
from datetime import date
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

# กำหนด css ปุ่ม
stylesheet="""
            QPushButton#add{
                background-color:#33FF00;
                color:white;
                font-size:14px;
                padding:5px;
                border: none;
                border-radius: 5px;
            }
            QPushButton#edit{
                background-color:#3399FF;
                color:white;
                font-size:14px;
                padding:5px;
                border: none;
                border-radius: 5px;
            }
            QPushButton#delete{
                background-color:#CC3333;
                color:white;
                font-size:14px;
                padding:5px;
                border: none;
                border-radius: 5px;
            }
            QPushButton#update{
                background-color:#FF33CC;
                color:white;
                font-size:14px;
                padding:5px;
                border: none;
                border-radius: 5px;
            }
            QPushButton#add:hover,QPushButton#edit:hover,QPushButton#delete:hover,QPushButton#update:hover{
                background-color:#FFD700;
                color:black;
            }
"""


class MainWindow(QMainWindow):
    _dev = "Valentinote"

    def __init__(self):
        super().__init__()
        # ข้อมูลเริ่มต้น
        self.products = [
            {'name':'iphone','price':500,'description':'This is an Iphone'},
            {'name':'ipad','price':1500,'description':'This is an Ipad'},
            {'name':'imac','price':2500,'description':'This is an Imac'},
        ]
        self.conn = sqlite3.connect("products.db")
        self.create_table()
        self.edit = False
        self.initUI()
    # method สร้างฐานข้อมูล ดาต้าเบส SQLite
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       price INTEGER,
                       description TEXT,
                       quantity INTEGER
                )
            """)
        self.conn.commit()
    
    # method อ่านข้อมูล ในดาต้าเบส SQLite
    def load_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        # กำหนด แถว ตามข้อมูลที่ดึงออกมา
        self.table_widget.setRowCount(len(products))
        # ดึงข้อมูลสินค้าออกมาแสดงที่ตาราง
        for row,product in enumerate(products):
            for col,value in enumerate(product):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row,col,item) 
    
    def initUI(self):
        # กำหนด ขั้นต่ำการของหน้าจอ setMinimumSize(w,h)
        self.setMinimumSize(600,500)
        # กำหนด ชื่อหน้าจอ
        self.setWindowTitle("จัดการสต๊อกสินค้า")

        # สร้างหน้าต่างหลัก
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # สร้างตารางรายการสินค้า
        self.table_widget = QTableWidget(self)
        layout.addWidget(self.table_widget)
        self.table_widget.setAlternatingRowColors(True)

        # กำหนด คอลัมน์
        self.table_widget.setColumnCount(5)
        # กำหนดชื่อหัวตาราง คอลัมน์
        self.table_widget.setHorizontalHeaderLabels(["ID","ชื่อสินค้า","ราคา","รายละเอียดสินค้า","จำนวนสินค้า"])
        # เรียกใช้งาน method ดึงข้อมูลจาก ดาต้าเบส
        self.load_data()
              
        # สร้างฟอร์มบันทึกข้อมูลสินค้า
        self.name_edit =QLineEdit(self)
        self.price_edit =QLineEdit(self)
        self.description_edit =QLineEdit(self)
        self.quantity_edit =QLineEdit(self)
        layout.addWidget(QLabel("ชื่อสินค้า :"))
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("ราคา :"))
        layout.addWidget(self.price_edit)
        layout.addWidget(QLabel("รายละเอียด :"))
        layout.addWidget(self.description_edit)
        layout.addWidget(QLabel("จำนวนสินค้า :"))
        layout.addWidget(self.quantity_edit)
        
        # เพิ่ม layout จัดเรียง ปุ่ม แบบ แนวนอน
        btn_layout1 = QHBoxLayout()
        btn_layout2 = QHBoxLayout()
        # ปุ่มบันทึกสินค้า
        add_button = QPushButton("เพิ่มสินค้า",self)
        add_button.setObjectName('add')
        add_button.clicked.connect(self.add_product)
        btn_layout1.addWidget(add_button)
        # ปุ่มอัพเดทข้อมูลสินค้า
        edit_button = QPushButton("แก้ไขข้อมูล",self)
        edit_button.setObjectName('edit')
        edit_button.clicked.connect(self.edit_product)
        btn_layout1.addWidget(edit_button)
        layout.addLayout(btn_layout1)

        # ปุ่มลบสินค้า
        delete_button = QPushButton("ลบสินค้า",self)
        delete_button.setObjectName('delete')
        delete_button.clicked.connect(self.delete_product)
        btn_layout2.addWidget(delete_button)
        # ปุ่มอัพเดทข้อมูลสินค้า
        update_button = QPushButton("อัพเดทสินค้า",self)
        update_button.setObjectName('update')
        update_button.clicked.connect(self.update_product)
        btn_layout2.addWidget(update_button)
        layout.addLayout(btn_layout2)

        year = date.today().year
        modify_dev = QLabel(self)
        modify_dev.setText(f"Copyright @{year} พัฒนาโดย {self._dev}")
        modify_dev.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(modify_dev)

    # method ต่างๆ
    def add_product(self): # ฟังก์ชั่นเพิ่มสินค้า
        # ดึงข้อมูลมาเก็บลงในตัวแปร
        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()
        quantity = self.quantity_edit.text().strip()
        if name !="" and price !="" and description !="" and quantity !="":
            # เพิ่มข้อมูลลงใน ดาต้าเบส SQLite
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO products (name,price,description,quantity) VALUES (?,?,?,?)',(name,price,description,quantity))
            self.conn.commit()
            # แจ้งเตือนหลังจากเพิ่มข้อมูลเสร็จ
            QMessageBox.information(self,"แจ้งเตือน","เพิ่มข้อมูลเรียบร้อยแล้ว!!")
            # โหลดข้อมูลซ้ำในตาราง
            self.load_data()
            # เคลียร์ข้อมูลในช่องฟอร์มบันทึก
            self.name_edit.clear()
            self.price_edit.clear()
            self.description_edit.clear()
            self.quantity_edit.clear()
        else:
            QMessageBox.warning(self,"แจ้งเตือน","ระบุข้อมูลไม่ครบ กรุณาตรวจสอบก่อน กดปุ่ม ' เพิ่มสินค้า '")
        

    def delete_product(self): # ฟังก์ชั่นลบสินค้า
        try:
            # ดึงข้อมูลจากช่องกรอก มาเก็บลงในตัวแปร
            name = self.name_edit.text().strip()
            # ดึงข้อมูลจากตาราง (ID) มาเก็บลงในตัวแปร
            product_id = int(self.table_widget.item(self.current_row,0).text())
            # แจ้งเตือน ให้ยืนยันก่อนทำการลบสินค้า
            choice = QMessageBox.question(self,'แจ้งเตือน',f'คุณต้องการลบข้อมูลสินค้า {name} ตัวนี้หรือไม่ ?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if choice == QMessageBox.StandardButton.Yes:
                # คำสั่งลบข้อมูล ใน ดาต้าเบส
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM products WHERE id=?",(product_id,))
                self.conn.commit()
                # แจ้งเตือนหลังจากลบข้อมูลเสร็จ
                QMessageBox.information(self,'แจ้งเตือน','ลบข้อมูลสินค้าเรียบร้อย')
                # โหลดข้อมูลซ้ำในตาราง
                self.load_data()
        except AttributeError:
            QMessageBox.warning(self,"แจ้งเตือน","กรุณาเลือกแถวและกดปุ่ม ' แก้ไขข้อมูล ' ก่อนทำการกดปุ่ม ' ลบข้อมูล '")
    
    def update_product(self): # ฟังก์ชั่นอัพเดทสินค้า 
        try:
            # ดึงข้อมูลจากช่องกรอก มาเก็บลงในตัวแปร
            name = self.name_edit.text().strip()
            price = self.price_edit.text().strip()
            description = self.description_edit.text().strip()
            quantity = self.quantity_edit.text().strip()
            # ดึงข้อมูลจากตาราง (ID) มาเก็บลงในตัวแปร
            product_id = int(self.table_widget.item(self.current_row,0).text())
            if name !="" and price !="" and description !="" and quantity !="":
                # คำสั่งอัพเดทข้อมูล ใน ดาต้าเบส
                cursor = self.conn.cursor()
                cursor.execute("UPDATE products SET name=?, price=?, description=?,quantity=? WHERE id=?",(name,price,description,quantity,product_id))
                self.conn.commit()
                # แจ้งเตือนหลังจากอัพเดทเสร็จ
                QMessageBox.information(self,"แจ้งเตือน","ทำการอัพเดทข้อมูลเรียบร้อยแล้ว!!")
                # โหลดข้อมูลซ้ำในตาราง
                self.load_data()
                # เคลียร์ข้อมูลในช่องฟอร์ม
                self.name_edit.clear()
                self.price_edit.clear()
                self.description_edit.clear()
                self.quantity_edit.clear()
        except AttributeError:
            QMessageBox.warning(self,"แจ้งเตือน","กรุณาเลือกแถวและกดปุ่ม ' แก้ไขข้อมูล ' ก่อนทำการกดปุ่ม ' อัพเดทข้อมูล '")

    def edit_product(self): # ฟังก์ชั่นดึงข้อมูลจากตารางมาแสดงในช่องฟอร์มกรอกข้อมูล
        self.current_row = self.table_widget.currentRow()
        # นำข้อมูลที่ดึงมาไปแสดงในช่อง ฟอร์มกรอกข้อมูล
        self.name_edit.setText(self.table_widget.item(self.current_row,1).text())
        self.price_edit.setText(self.table_widget.item(self.current_row,2).text())
        self.description_edit.setText(self.table_widget.item(self.current_row,3).text())
        self.quantity_edit.setText(self.table_widget.item(self.current_row,4).text())
        

app = QApplication(sys.argv)
# เรียกใช้งาน css
app.setStyleSheet(stylesheet)
window = MainWindow()
# กำหนด icon ให้หน้าต่าง
window.setWindowIcon(QIcon("./icons/inventory_icon.png"))
window.show()
sys.exit(app.exec())