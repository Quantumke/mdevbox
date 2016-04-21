from mdevbox.models import developers_portfolio
from mdevbox.models import appliedcandidates

class ApplyJob():
	def run(data,request):
		user=request.user
		#print(user)
		instance=developers_portfolio.objects.get(email=user)
		portfolio_link=instance.portfoli_link
		applicant=user
		save=appliedcandidates(applicant=applicant, portfolio_link=portfolio_link)
		save.save()

