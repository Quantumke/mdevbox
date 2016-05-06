from mdevbox.models import developers_portfolio
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class SendEmailNotification():
	def run(data, id):
		instance=developers_portfolio.objects.get(id=id)
		email=instance.email
		hire_data=data.get('hire_data')
		company=hire_data.get('company')
		job_title=hire_data.get('job_title')
		job_description=data.get('job_description')
		subject = "Someone wants to hire you!"
		subject, from_email, to = subject, settings.EMAIL_HOST_USER, email
		text_content = 'Someone found your portfolio and is interested'
		html_content = "<p>Someone found your portfolio and is interested</p>"
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
		print(email)

