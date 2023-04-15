from django.urls import path
from.import views
urlpatterns = [
    path('he_page',views.test_app01),
    path('test_001',views.test_app02),
    path('stud_datasheet',views.student_sheet),
    path('update/<int:id>',views.updates),
    path('delect/<int:id>',views.delect_sheet),
    path('add',views.add_sheet)
]
