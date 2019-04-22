import pymysql
import bleach

class Notifications:
    
    def __init__(self, uid, host, username, password, database, adminpassword):
        self.uid = bleach.clean(uid)
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.adminpassword = adminpassword

    def register_device(self, device_id, platform):
        conn = pymysql.connect(self.host, self.username, self.password, self.database)
        cursor = conn.cursor()
    
        cursor.execute("INSERT INTO devices(device_id, uid, platform ) VALUES(" + device_id + "," + self.uid + "," + platform + ");")
        
        conn.commit()
        conn.close()

    #def send_notification(self, title, message):
        #TODO send notifications here we'll probably be using FCM 
