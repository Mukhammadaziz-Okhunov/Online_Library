from django.contrib import admin
from django.urls import path
from library.views import home, kitoblar, mualliflar, kitob1, muallif1, recordlar, record1


# from library.views import kitob
# from library.views import muallif
# from library.views import katta_muallif
# from library.views import record
# from library.views import ilmiy
# from library.views import erkak
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<str:ism>', home),
    path('kitoblar/', kitoblar, name='kitoblar'),
    path('mualliflar/', mualliflar, name='mualliflar'),
    path('kitoblar/<int:son>', kitob1, name='kitob1'),
    path('mualliflar/<int:son>', muallif1, name='muallif1'),
    path('recordlar/<int:son>', record1, name='record1'),
    path('recordlar/', recordlar, name='recordlar'),


    # path('Kitob/', kitob),
    # path('m/', muallif),
    # path('katta_muallif/', katta_muallif),
    # path('record/', record),
    # path('ilmiy/', ilmiy),
    # path('erkak/', erkak),

]































