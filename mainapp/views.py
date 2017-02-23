from django.shortcuts import render

from django.http import HttpResponse
class Entry():
	def __init__(self,title,body, img_url ):
	  self.title = title
          self.body = body
          self.img_url = img_url
def index(request):
        entrys =[
        Entry("primer post"," aprendiendo envi dinamico atemplate", "http://static.notinerd.com/wp-content/uploads/2017/02/58a5a2e2759ec.jpeg "),
        Entry("segundo post"," ojo un post nuevo "," http://notinerd.com/galeria-la-empresa-que-convierte-dibujos-de-ninos-en-juguetes/")
        ]
        entrys_total = len(entrys)

	return render(request, "index.html",{'entrys':entrys,'entrys_totl':entrys_total})


