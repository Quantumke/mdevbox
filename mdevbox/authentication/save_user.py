from django.contrib.auth.models import User
from mdevbox.models import reg_user
class SaveUser():
	def run(data):
		new_user=data.get('new_user')
		new_user=User(**new_user)
		password=new_user.password
		#print(password)
		new_user.set_password(password)
		#new_user.save()
		data['user']=new_user
