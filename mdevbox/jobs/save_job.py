from mdevbox.models import post_job
class SaveJob():
	def run(data):
		job_data=data.get('job_data')
		company=job_data.get('company')
		job_title=job_data.get('job_title')
		job_description=job_data.get('job_description')
		pay=job_data.get('pay')
		print(job_title, job_description, pay)
		save=post_job(company=company, job_title=job_title, job_description=job_description, pay=pay)
		save.save()

