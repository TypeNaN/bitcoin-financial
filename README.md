## bitcoin-financial

#### การเตรียมสภาพแวดล้อมในการพัฒนา
###### bitcoin-financial ถูกพัฒนาบนระบบ

~~~bash
	Linux 3.19.0-43-generic #49~14.04.1-Ubuntu SMP Thu Dec 31 15:44:49 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
~~~

###### เตรียมเครื่องมือที่ใช้ในการพัฒนา

~~~bash
	sudo apt-get update
	sudo apt-get upgrade -y
	sudo apt-get install python-qt4 pyqt4-dev-tools qt4-designer
	git clone https://github.com/Yanatecho/bitcoin-financial.git
~~~

###### ทดสอบเครื่องมือที่ใช้ในการพัฒนาโดยสร้างโปรเจ็คท์ใหม่ (ข้ามไปหัวข้อถัดไปเลยก็ได้)

+ ลำดับที่หนึ่ง
~~~bash
	+ เปิด qt4-designer ขึ้นมา
	+ ภายใน startup dialog จะต้องสร้าง New Form ขึ้นมา โดยในช่อง templates/forms ให้เลือก Main Windows
	+ คลิกที่ Create
~~~


