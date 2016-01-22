## bitcoin-financial

#### การเตรียมสภาพแวดล้อมในการพัฒนา
###### bitcoin-financial ถูกพัฒนาบนระบบ

~~~
	Linux 3.19.0-43-generic #49~14.04.1-Ubuntu SMP Thu Dec 31 15:44:49 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
~~~

###### เตรียมเครื่องมือที่ใช้ในการพัฒนา

~~~
	sudo apt-get update
	sudo apt-get upgrade -y
	sudo apt-get install python-qt4 pyqt4-dev-tools qt4-designer
	git clone https://github.com/Yanatecho/bitcoin-financial.git
~~~

###### ทดสอบเครื่องมือที่ใช้ในการพัฒนาโดยสร้างโปรเจ็คท์ใหม่ (ข้ามไปหัวข้อถัดไปเลยก็ได้)

+ ลำดับที่หนึ่ง
	1. เปิด qt4-designer ขึ้นมา
	2. ภายใน startup dialog จะต้องสร้าง New Form ขึ้นมา โดยในช่อง templates/forms ให้เลือก Main Windows
	3. คลิกที่ Create
	4. ออกแบบหน้าตาของโปรแกรมตามใจชอบ (อาจใช้เวลานิดนึงสำหรับวางองค์ประกอบต่างๆ)
	5. เสร็จแล้วบันทึกไฟล์เป็น main.ui

+ ลำดับที่สอง
	1. แปลงไฟล์ .ui ที่ออกแบบไว้ให้เป็น .py ด้วย pyuic4

	~~~
		pyuic4 main.ui -o main.py
	~~~
