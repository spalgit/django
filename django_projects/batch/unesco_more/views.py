from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

from unesco_more.models import Category, States, Region, Iso, Site


class SiteView(LoginRequiredMixin, View):
    def get(self,request):
        x = Site.objects.all()[:20]
        ctx = {'site_list': x}
        print("ctx = {}".format(ctx))
        return render(request, 'unesco_more/site_list.html', ctx)

class DetailView(LoginRequiredMixin,View):
    def get(self,request,site_id):
        region = Site.objects.get(pk=site_id).region
        category = Site.objects.get(pk=site_id).category
        states = Site.objects.get(pk=site_id).states
        iso = Site.objects.get(pk=site_id).iso
        ctx = {'region': region, 'category': category, 'states': states, 'iso': iso}
        print("ctx = {}".format(ctx))
        return render(request, 'unesco_more/region_list.html', ctx)


# class RegionView(LoginRequiredMixin, View):
#     def get(self, request, site_id):
#         rg = Region.objects.filter()
#         # print("The sites are = {}".format(sl))
#
#         ctx = {'region_list': rg}
#         print("The region list = {}".format(ctx))
#         return render(request, 'unesco/region_list.html', ctx)
