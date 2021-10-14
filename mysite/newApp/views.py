from django.shortcuts import render

def helloWorld(request):
    return render(request, 'helloWorld.html', {})

def fourImages(request):
    img = ["https://hotdogchecker.s3.amazonaws.com/falseHotDog7.jpg", "https://hotdogchecker.s3.amazonaws.com/trueHotDog7.jpg"]
    images = zip(img)
    return render(request,'test_zip_clecle.html',{"images":images})