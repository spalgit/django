from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

from unesco.models import Category, States, Region, Iso, Site


class RegionView(LoginRequiredMixin, View):
    def get(self, request):
        rg = Region.objects.all()[:10]
        # print("The sites are = {}".format(sl))

        ctx = {'region_list': rg}
        print("The region list = {}".format(ctx))
        return render(request, 'unesco/region_list.html', ctx)

class SiteDetailView(LoginRequiredMixin, View):
    def get(self,request,region_id):
        x = Site.objects.filter(region = region_id )[:10]
        ctx = {'site_list': x}
        print("ctx = {}".format(ctx))
        return render(request, 'unesco/site_list.html', ctx)
