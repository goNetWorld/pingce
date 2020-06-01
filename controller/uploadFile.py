from controller.init import *
import os,time
from hashlib import md5

class FileUpload(MainController):
    def get(self):
        self.write("Hello, world")
    # @tornado.web.authenticated
    def post(self):
        try:
            upload_path = os.path.join(os.path.dirname(__file__),"..","static", 'files')
            # 提取表单中‘name’为‘file’的文件元数据
            file_metas = self.request.files['file']
            for meta in file_metas:
                filename = meta['filename']
                fileAttr=str(filename).rsplit('.')
                if(len(fileAttr)<2):
                    raise FileNotFoundError
                fileProFix=fileAttr[-1]
                timeMd5=md5("saltCode".encode("utf-8"))
                timeMd5.update(str(time.time()).encode('utf-8'))
                newFileName =str(timeMd5.hexdigest())+"."+fileProFix
                filepath = os.path.join(upload_path, newFileName)
                # 有些文件需要已二进制的形式存储，实际中可以更改
                with open(filepath, 'wb') as up:
                    up.write(meta['body'])
                self.toJson(0, '/static/files/'+newFileName)
        except Exception as e:
            print(e)
            self.toJson(1, '文件存储失败!')
