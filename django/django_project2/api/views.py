import requests
import xml.etree.ElementTree as ET

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


def index(request):
    return render(request, 'api/index.html')


@require_http_methods(["POST"])
def get_books(request):
    query = request.POST.get("query")
    url = "https://www.goodreads.com/search.xml?key=1QM7Oy1POPeFEC6R9NWTA%"
    res = requests.get(url, params={"q": query})

    xml_response = res.content

    root = ET.fromstring(xml_response)
    titles = [item.text for item in root.findall('.search/results/work/best_book/title')]
    covers = [item.text for item in root.findall('.search/results/work/best_book/image_url')]

    books = zip(titles, covers)

    return render(request, 'api/books.html', {
        "books": books
    })