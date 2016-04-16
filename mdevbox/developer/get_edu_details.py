class GetEduDetails():
	def run(data, request_data):
		data['edu_details']=GetEduDetails.get_details(request_data)

	def get_details(request_data):
		edu_details={}
		edu_details['highest_education']=request_data.get('highest_education')
		edu_details['institute_name']=request_data.get('institute_name')
		edu_details['course']=request_data.get('course')
		edu_details['begin_education']=request_data.get('begin_education')
		edu_details['end_education']=request_data.get('end_education')
		return edu_details