from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.response import TemplateResponse


    
def postLinksImages(request, template_name='page.html'):
    args = {}  

    args['mytext'] = ["https://hotdogchecker.s3.amazonaws.com/falseHotDog7.jpg", "https://hotdogchecker.s3.amazonaws.com/trueHotDog7.jpg"]
    return TemplateResponse(request, template_name, args)




