# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def parsed_list(request):
	posts = ()
	'''posts = (
		{"rownumber": 1,
 "title": "Google.ai",
 "autor": "rbanffy",
 "url": "https://google.ai",
 "site": "google.ai",
 },
{"rownumber": 2,
 "title": "A Case of Stolen Source Code",
 "autor": "uptown",
 "url": "https://panic.com/blog/stolen-source-code/",
 "site": "panic.com",
 },
{"rownumber": 3,
 "title": "Android now supports the Kotlin programming language",
 "autor": "JOfferijns",
 "url": "https://venturebeat.com/2017/05/17/android-now-supports-the-kotlin-programming-language/",
 "site": "venturebeat.com",
 },
{"rownumber": 4,
 "title": "Elf Hello World",
 "autor": "rocky1138",
 "url": "http://www.cirosantilli.com/elf-hello-world/",
 "site": "cirosantilli.com",
 },
{"rownumber": 5,
 "title": "JSON Feed",
 "autor": "fold",
 "url": "https://jsonfeed.org/2017/05/17/announcing_json_feed",
 "site": "jsonfeed.org",
 })'''


	return render(request, 'index.html', {"posts": posts})