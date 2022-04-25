from datetime import datetime


class NewFolder :
    def __int__(self,name) :
        self.subFolder = []
        self.name = name
        self.upload_time = datetime.now.strftime("%H:%M:%S %B %d, %Y")