โปรเจค CRUD PyQt6 inventory จัดการข้อมูล ระบบสต๊อกสินค้า พัฒนาโดยใช้ Python 3.12.2
1. สามารถนำไปพัฒนาใช้งานในรูปแบบอื่นๆได้ ผู้ใช้ จะต้องแก้ไขโค้ดเอาเอง
2. มีตัวโปรแกรมที่ทำการ deploy แล้ว ให้ทดสอบ อยู่ในโฟลเดอร์ output ก็อปปี้โฟลเดอร์ไปวางไว้หน้า desktop แล้วกดเข้าใช้งาน ตัว demo.exe

สำหรับผู้ที่จะนำไปใช้งานด้านอื่นๆ หรือ พัฒนาต่อยอดโปรแกรม
1. ให้ติดตั้ง โปรแกรม Editor VsCode
2. ติดตั้ง Extention คือ 1. Python 2. SQLite Viewer
3. ทำการ ดาวโหลด python 3.12.x และติดตั้งลงเครื่อง
4. เปิด Command Prompt (cmd) และทำการ install PyQt6 โดยใช้คำสั่ง pip install PyQt6  
5. ทำการแก้ไขไฟล์ ด้านในจะมี comment รายละเอียดต่างๆ ให้ชัดเจน

ปล. ฐานข้อมูลดาต้าทั้งหมด จะจัดเก็บที่ตัวเครื่องของผู้ใช้งาน หรือ localstorage ตัวฐานข้อมูล เป็นตัวที่ติดมากับ Python คือ SQLite3

หมายเหตุ : โปรแกรมนี้จัดทำขึ้นเพื่อเป็นแนวทางในการศึกษา พัฒนา ฝึกเขียนโค้ดจัดการฐานข้อมูล เท่านั้น 
ซึ่งหากผู้ที่นำไปพัฒนาต่อหรือนำไปใช้งาน และเกิดความเสียหายแกตัวคุณเอง ทางผมไม่รับผิดชอบ ใดๆ ทั้งสิ้น เนื่องจากตัวโปรแกรมเป็นตัวทดสอบและแจกฟรี
เพื่อให้ศึกษาเกี่ยวกับตัวโค้ดเท่านั้น ยังไม่มีเช็คเรื่องป้องกันความปลอดภัยของข้อมูล และ อื่นๆ

ภาษาที่ใช้เขียน : Python
ไลบารี่ : PyQt6
ดาต้าเบส : SQLite3

# พัฒนาโดย Valentinote
ช่องทางติดต่อ ผ่านเฟสบุ๊ค : https://www.facebook.com/profile.php?id=100058065267269
ตอบช้าหน่อยนะครับ.
