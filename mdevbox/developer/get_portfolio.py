class GetPortfolio():
	def run(request_data,data):
		data['portfolio']=GetPortfolio.get_portfolio(request_data)
		#print (request_data)

	def get_portfolio(request_data):
		portfolio={}
		portfolio['portfoli_name'] = request_data.get('portfoli_name')
		portfolio['portfoli_tech'] = request_data.get('portfoli_tech')
		portfolio['portfoli_link'] = request_data.get('portfoli_link')
		portfolio['portfoli_desc'] = request_data.get('portfoli_desc')
		return portfolio

