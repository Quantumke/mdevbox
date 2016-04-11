class GetUserDetails():
	def run(request_data, data):
		data['new_user']=GetUserDetails.get_post_data(request_data)
		#print(request_data)
		
	def get_post_data(request_data):
		new_user={}
		new_user['username']=request_data.get('username')
		new_user['first_name']=request_data.get('first_name')
		new_user['last_name']= request_data.get('last_name')
		new_user['email']=request_data.get('email')
		new_user['password']=request_data.get('password')
		return new_user
