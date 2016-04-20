class GetWorkDetails():
	def run(request_data,data):
		data['work_data']=GetWorkDetails.get_work_data(request_data)
		#print (request_data)

	def get_work_data(request_data):
		work_data={}
		work_data['email']=request_data.get('email')
		work_data['speciality'] = request_data.get('speciality')
		work_data['previous_employer'] = request_data.get('previous_employer')
		work_data['role_previous_employment'] = request_data.get('role_previous_employment')
		work_data['begin_previous_employment'] = request_data.get('begin_previous_employment')
		work_data['end_previous_employment']= request_data.get('end_previous_employment')
		return  work_data


