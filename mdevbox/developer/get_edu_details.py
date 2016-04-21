class GetEduDetails():

	def run(request_data,data):
		data['edu_data']=GetEduDetails.get_edu_data(request_data)
		print (request_data)

	def get_edu_data(request_data):
		edu_data={}
		edu_data['course']=request_data.get('course')
		edu_data['highest_education']=request_data.get('highest_education')
		edu_data['institute_name']=request_data.get('institute_name')
		edu_data['begin_education']=request_data.get('begin_education')
		edu_data['end_education']=request_data.get('end_education')
		return  edu_data

