from datetime import datetime


class NewFile:
    def __int__(self,name,type,size, upload_time= datetime.now()):
        self.name = name
        self.type = type
        self.size = size
        self.upload_time = upload_time.strftime("%H:%M:%S %B %d, %Y")