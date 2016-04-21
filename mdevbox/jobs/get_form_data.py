class GetFormData():
	def run(request_data,  data):
		data['job_data']=GetFormData.get_data(request_data)
		print(request_data)
	def get_data(request_data):
		job_data={}
		job_data['company']=request_data.get('company')
		job_data['job_title']= request_data.get('job_title')
		job_data['job_description']= request_data.get('job_description')
		job_data['pay']=request_data.get('pay')
		return job_data
