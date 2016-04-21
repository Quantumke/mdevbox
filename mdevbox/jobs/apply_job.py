from mdevbox.models import developers_portfolio
class ApplyJob():
	def run(data, id):
		instance=developers_portfolio.objects.get(id=id)
		email=instance.email
		print(email)
