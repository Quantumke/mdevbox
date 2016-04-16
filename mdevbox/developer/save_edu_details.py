from mdevbox.models import developers_education
class SaveEduDetails():
	def run(data):
		edu_details=data.get('edu_details')
		work_details=data.get('work_details')
		email=work_details.get('email')
		highest_education=edu_details.get('highest_education')
		institute_name=edu_details.get('institute_name')
		course=edu_details.get('course')
		begin_education=edu_details.get('begin_education')
		end_education=edu_details.get('end_education')
		save=developers_education(email=email,highest_education=highest_education, institute_name=institute_name, course=course,begin_education=begin_education, end_education=end_education )
		save.save()
		data['edu_details']=edu_details
