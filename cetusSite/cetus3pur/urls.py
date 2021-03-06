from django.urls import path
from . import views

urlpatterns = [
        # ex: /cetus3pur/
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),

        # ex: /cetus3pur/userprofile/
    path('userprofile/', views.userprofile, name='CetusUser_Profile'),

        # view all 3rd parties
        # ex: /cetus3pur/tpv
    path('tpv/', views.ThirdPartiesView, name='ThirdPartiesView'),

        # view users for a specific 3rd party business
        # ex: /cetus3pur/tpvu
    path('tpvu/<int:thirdparty_id>/', views.ThirdPartyUsersTableView, name='ThirdPartyUsersTableView'),

        # view specific user
        # ex: /cetus3pur/user/1
    path('user/<int:user_id>/', views.ThirdPartyUserViewEdit, name='userviewedit'),

        # add new third party users
        # ex: /cetus3pur/AddNewUsers/1
    path('addusers/<int:thirdparty_id>', views.ThirdPartyUsersAdd, name='AddNewUsers'),

        # view RR managers
        # ex: /cetus3pur/rrm
    path('rrm/', views.RRRManagersView, name='RRRManagersView'),

    # path('eabreq/',views.EAB_RequestCreate, name='EAB_RequestCreate'),
    path('eabreq/create/',views.EAB_RequestCreate_cbv.as_view()),
    path('eabreq/edit/<int:pk>',views.EAB_RequestEdit_cbv.as_view()),
    path('eabreq/view/<int:pk>',views.EAB_RequestView_cbv.as_view()),

    path('eabappr/create/',views.EAB_ApproveCreate_cbv.as_view()),  ## creating with no specified request in mind, user selects request on form
    path('eabappr/create/<int:reqid>',views.EAB_ApproveCreate_cbv.as_view()), ## creating with a selected request, can't be changed on form
    path('eabappr/edit/<int:pk>',views.EAB_ApproveEdit_cbv.as_view()),
    path('eabappr/view/<int:pk>',views.EAB_ApproveView_cbv.as_view()),

    path('datastoresystems_cbv/',views.datastoresystems_cbv, name='datastoresystems_cbv'),

    path('eabreq_for_approval/',views.EAB_ReviewSelect, name='EAB_ReviewSelect'),

    ##18 -- path('eabreviewapprove/<int:approval_id>',views.EAB_ReviewApprove, name='EAB_ReviewApprove'),
    ##18 -- path('eabreviewapprove/',views.EAB_ReviewApprove, name='EAB_ReviewApprove'),

    ##18 -- path('eabrecords/',views.EAB_Records, name='EAB_Records'),
    
    # for debugging first Class based view  
    path('eabrecords_cbv/',views.EAB_Records_cbv.as_view()),
    
    path('audit/',views.Audit, name='Audit'),
	
    path('IT_actionlog/',views.IT_ActionLog, name='IT_actionlog'),
]

