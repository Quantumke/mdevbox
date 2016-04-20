from mdevbox.models import hire
class SaveHire():
	def run(data):
		hire_data=data.get('hire_data')
		company=hire_data.get('company')
		job_title=hire_data.get('job_title')
		job_description=hire_data.get('job_description')
		save=hire(company=company, job_title=job_title, job_description=job_description)
		save.save()

