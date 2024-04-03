from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import ElectricShopForm
from .models import ElectricShop


class ElectricView(View):
    template_name = "curd_app/info.html"
    form = ElectricShopForm

    def get(self, request):
        form = self.form()
        context = {"form": form}
        return render(request,self.template_name, context)

    def post(self,  request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        return render(request, self.template_name, {"form": form})


class ShowView(View):
    template_name = "curd_app/show.html"
    form = ElectricShopForm

    def get(self, request):
        form = self.form()
        obj = ElectricShop.objects.all()
        context = {"obj": obj, "form": form}

        return render(request, self.template_name, context)

    def post(self , request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_url')
        return render(request, self.template_name, {"form": form})


class UpdateView(View):
    template_name = "curd_app/info.html"
    form = ElectricShopForm

    def get(self, request, pk):
        objs = ElectricShop.objects.get(id=pk)
        form = self.form(instance=objs)
        context = {"objs": objs, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        objs = ElectricShop.objects.get(id=pk)
        form = self.form(request.POST, instance=objs)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        return render(request, self.template_name, {"form": form})


class DeleteView(View):
    template_name = "curd_app/confirm.html"
    form = ElectricShopForm

    def get(self, request, pk):
        objs = ElectricShop.objects.get(id=pk)
        form = self.form(instance=objs)
        context = {"objs": objs, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj = ElectricShop.objects.get(id=pk)
        obj.delete()
        return redirect("show_url")
