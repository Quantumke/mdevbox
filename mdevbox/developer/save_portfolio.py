from mdevbox.models import developers_portfolio
class SavePortfolio():
	def run(data, request):
		portfolio=data.get('portfolio')
		work_details=data.get('work_data')
		email=request.user
		portfoli_name=portfolio.get('portfoli_name')
		portfoli_tech=portfolio.get('portfoli_tech')
		portfoli_link=portfolio.get('portfoli_link')
		portfoli_desc=portfolio.get('portfoli_desc')
		print (portfoli_desc, portfoli_link)
		save=developers_portfolio(email=email, portfoli_name=portfoli_name, portfoli_tech=portfoli_tech,portfoli_link=portfoli_link,portfoli_desc=portfoli_desc)
		save.save()

