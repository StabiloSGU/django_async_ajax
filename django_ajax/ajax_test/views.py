from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers
from asgiref.sync import sync_to_async
from random import randint, choice
from asyncio import sleep


from django.template import loader
from ajax_test.forms import AjaxForm
from ajax_test.models import FileUpload


#time consuming task
async def time_consuming_task(file):
    file_to_work = file
    #set file to working
    file.status = FileUpload.WORKING
    await sync_to_async(file.save)()
    time_to_work = randint(10,30)
    random_outcome = choice([FileUpload.SUCCESS, FileUpload.ERROR])
    #wait for random time and give random outcome
    await sleep(time_to_work)
    file.status=random_outcome
    await sync_to_async(file.save)()



async def index(request):
    # ignore IDE error
    filelist = await sync_to_async(list)(FileUpload.objects.all())
    return render(
        request,
        'ajax_test/index.html',
        {
            "form" : AjaxForm,
            "files" : filelist,
        }
    )

async def ajx(request):
    if request.method == 'POST':
        form = AjaxForm(request.POST, request.FILES)
        if form.is_valid():
            obj = await sync_to_async(form.save)()
            await time_consuming_task(obj)
            return JsonResponse({"message": 'Success!'}, status=200)
        else:
            return JsonResponse({"message": 'Form is not valid!'}, status=403)

async def get_filelist(request):
    # ignore IDE error
    filelist = await sync_to_async(list)(FileUpload.objects.all())
    ser_filelist = serializers.serialize('json', filelist)
    return JsonResponse({"instance": ser_filelist}, status=200)