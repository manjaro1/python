from gcmpush import *

regid="APA91bHI6bvE3xnbAF6f1YqRbRTMck6bxqzZtj-97JfVHbmsgKXcJeFyT-cOKRKIf3eVm-mBvwi4DNzcrmhQtcCWpQsWWnyYDaCEFMCDsIUbqtnk3bdjs3acJV2TwwByE-BopE26moyx1Q2xg-YK75asdDUxUJ2fbSS6vcnuEzswIfnYRN-4Z3w"

json_data = { "registration_id": regid, "data" : {
		"reg_id": regid,
		 "tipo": 2,
		 "statustiempo": "2",
		 "mensaje":'cuauhtemoc se la come'
		        },
		    }



enviopush(json_data)