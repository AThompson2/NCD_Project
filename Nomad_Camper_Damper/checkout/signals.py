from django.shortcuts import get_object_or_404
from .models import Order
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import weasyprint
from io import BytesIO


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        order = get_object_or_404(Order, id=ipn.invoice)

        if order.total_cost() == ipn.mc_gross:
            # mark the order as paid
            order.paid = True
            order.save()


            # Create Invoice e-mail
            subject = 'Nomad Camper Damper - Invoice no. {}'.format(order.id)
            message = 'Please, find attached the invoice for your recent purchase.'
            email = EmailMessage(subject,
                                 message,
                                 'NomadCamperDamper@gmail.com',
                                 [order.email])
            # Generate PDF
            html = render_to_string('checkout/pdf.html',{'order': order})
            out = BytesIO()
            stylesheets=[weasyprint.CSS(settings.STATIC_ROOT+'/css/pdf.css')]
            weasyprint.HTML(string=html).write_pdf(out,stylesheets=stylesheets)
            # Attach PDF files
            email.attach('order_{}.pdf'.format(order.id),
                          out.getvalue(),
                         'application/pdf')
            # Send Email
            email.send()
