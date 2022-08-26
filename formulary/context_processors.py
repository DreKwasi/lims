from .models import *


def major_links(request):
    cat_links = Category.objects.all()
    manu_links = Manufacturer.objects.all()
    gen_links = Generic_Attr.objects.all()
    form_links = Form.objects.all()

    return dict(
        cat_links=cat_links,
        manu_links=manu_links,
        gen_links=gen_links,
        form_links=form_links,
    )
