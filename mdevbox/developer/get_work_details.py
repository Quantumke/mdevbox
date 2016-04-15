class GetWorkDetails():
	def run(data, request_data):
		data['work_deails]=GetWorkDetails.get_details(request_data)


	def get_details(request_data):
		work_deails={}
		work_deails['email']=request_data.get('email')
		work_deails['speciality']=request_data.get('speciality')
		work_deails['previous_employer']=request_data.get('previous_employer')
		work_deails['role_previous_employment']=request_data.get('role_previous_employment')
		work_deails['begin_previous_employment']=request_data.get('begin_previous_employment')
		work_deails['end_previous_employment']=request_data.get('end_previous_employment')
		return work_deails
