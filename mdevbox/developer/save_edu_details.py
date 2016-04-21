from mdevbox.models import developers_education
class SaveEduDetails():
	def run(data,request):
		edu_details=data.get('edu_data')
		#print (edu_details)
		email=request.user
		highest_education=edu_details.get('highest_education')
		institute_name=edu_details.get('institute_name')
		course=edu_details.get('course')
		begin_education=edu_details.get('begin_education')
		end_education=edu_details.get('end_education')
		print (end_education)
		save=developers_education(email=email, highest_education=highest_education, institute_name=institute_name, course=course,begin_education=begin_education, end_education=end_education )
		save.save()
		data['edu_details']=edu_details
