from django.urls import path

from color_picker_app.views import ColorPickerView

urlpatterns = [
    path('', ColorPickerView.as_view(), name='color'),
]