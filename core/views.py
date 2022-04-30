from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

from brands.models import Brand

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {
	"company": "Alankar Restaurant & Bar",
	"address": "Gopapur,Naimnagar",
	"city": "Hanamkonda",
	"state": "Telangana",
	"zipcode": "506001",
	"phone": "7794821960",
	"email": "alankarrb@bar.com",
	"website": "alankarbar.com",
	}
brands =Brand.objects.all().order_by('ncode')

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('core/pdf_template.html', {'brands':brands,'data':data})
		return HttpResponse(pdf, content_type='application/pdf')
#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('core/pdf_template.html', {'brands':brands,'data':data})
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Brands_list.pdf"
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response



def index(request):
	context = {}
	return render(request, 'app/index.html', context)
