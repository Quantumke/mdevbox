from mdevbox.models import developers_employment
class SaveEmpDetails():
	def run(data, request):
		work_details=data.get('work_data')
		email=request.user
		speciality=work_details.get('speciality')
		previous_employer=work_details.get('previous_employer')
		role_previous_employment=work_details.get('role_previous_employment')
		begin_previous_employment=work_details.get('begin_previous_employment')
		end_previous_employment=work_details.get('end_previous_employment')
		print(begin_previous_employment, email)
		save=developers_employment(email=email, speciality=speciality, previous_employer=previous_employer, role_previous_employment=role_previous_employment, begin_previous_employment=begin_previous_employment, end_previous_employment=end_previous_employment)
		save.save()
