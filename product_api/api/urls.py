from django.urls import path

from . import views

urlpatterns = [
   
    # post 
    # get 
    path('chat-create/', views.Createchat, name='chat-create'),
    path('chat-list/', views.ShowChat, name='chat-list'),
    path('del-product/<str:pk>/',views.deleteProduct1),
    path('del-downloadexcel/<str:pk>/',views.deleteDownloadExcel),
    path('user-detail/<str:pk>/', views.ViewUser, name='user-detail'),
    path('product-list/', views.ShowAll, name='product-list'),
    path('product-detail/<int:pk>/', views.ViewProduct, name='product-detail'),

    # path('product-detail/<int:pk>/', views.ViewProduct, name='product-detail'), save-insert
    path('product-create/', views.CreateProduct, name='product-create'),
    path('product-update/<int:pk>/', views.updateProduct, name='product-update'),
    path('product-delete/<int:pk>/', views.deleteProduct, name='product-delete'),

    path('save/',views.saveform),
    path('save-mobile/',views.saveMobile),
    path('saved-list/', views.ShowsaveAll, name='downloadExcel-list'),
    path('saved-detail/<int:pk>/', views.ViewSaved, name='Saved-detail'),
    path('saved-detail-user/<str:pk>/', views.ViewSavedUser, name='Saved-detail-user'),
    path('saverecieved/',views.saverecieved1),
    path('saveinsert/',views.saveinsert),
    path('save-insert/',views.saveinsertform),

    path('report-delete/<int:pk>/',views.deleteReport),
    path('report-list/',views.ShowReportAll,name='Today Report'),
    path('report-insert/',views.reportInsert),

    path('unique-ac-list/',views.ShowAcAll,name='Show Accounts List '),

    path('', views.index, name="index"),
  
    path('uploadExcel/',views.uploadExcel,name='excelUpload'),

    # path('savereport/',views.saveReport1,name='excelDownload'),
    path('savereport/',views.saveReport1,name='excel Download'),

    path('readData/',views.readData,name='readData'),
    
    path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout"),

    path("privacypolicy/",views.privatePolicy)

     ]