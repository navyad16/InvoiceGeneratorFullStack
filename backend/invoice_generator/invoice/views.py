from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Invoice
from .serializers import InvoiceSerializer
import tempfile

# Create your views here.
from django.http import HttpResponse

@api_view(['POST'])
def create_invoice(request):
    serializer = InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        invoice = serializer.save()

        html_string = render_to_string('invoice.html', {'invoice': invoice})
        html = HTML(string=html_string)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as output:
            html.write_pdf(target=output.name)

        with open(output.name, 'rb') as pdf_file:
            pdf_content = pdf_file.read()

        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
        return response

    return Response(serializer.errors, status=400)
