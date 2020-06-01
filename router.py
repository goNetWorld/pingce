from tornado.web import *
from controller.index import *
from controller.login import *
from controller.writeTable import *
from controller.verificationTable import *
from controller.uploadFile import *
from admin.index import *
from controller.alterTable import *
from controller.printTable import *
Router=[
    (r"/index", IndexHandler),
    (r"/admin/index", AdminIndexHandler),
    (r"/login", LoginHandler),
    (r"/register", RegisterHandler),
    (r"/writeTable1", WriteTableOne),
    (r"/writeTable2", WriteTableTwo),
    (r"/writeTable3", WriteTableThree),
    (r"/alterTable1",AlterTableOne),
    (r"/alterTable2",AlterTableTwo),
    (r"/alterTable3",AlterTableThree),
    (r"/verificationTable1", VerificationTableOne),
    (r"/verificationTable2", VerificationTableTwo),
    (r"/verificationTable3", VerificationTableThree),
    (r"/printTable1", PrintTableOne),
    (r"/printTable2", PrintTableTwo),
    (r"/printTable3", PrintTableThree),
    (r"/alterPass", AlterPasswordHandler),
    (r"/resetPassword", ResetHandler),
    (r"/uploadFile", FileUpload),
    (r".*", LoginHandler),
]