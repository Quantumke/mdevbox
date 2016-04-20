class GetFormData():
	def run(request_data,  data):
		data['hire_data']=GetFormData.get_form_data(request_data)
		print(request_data)
	def get_form_data(request_data):
		hire_data={}
		hire_data['company']=request_data.get('company')
		hire_data['job_title']=request_data.get('job_title')
		hire_data['job_description']=request_data.get('job_description')
		return hire_data
