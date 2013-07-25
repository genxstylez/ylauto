from django.shortcuts import render, get_object_or_404
from gallery.models import Gallery, GalleryItem

def gallery_list(request):
    gallery_list = Gallery.objects.order_by('-created_at')
    return render(request, 'gallery/gallery-list.html', {'galleries': gallery_list})

def gallery_view(request, gallery_id):
    gallery = get_object_or_404(Gallery, id=gallery_id)
    items = gallery.items.all()
    f_item = items[0]
    return render(request, 'gallery/gallery.html', {'gallery': gallery, 'items': items, 'f_item' : f_item})
