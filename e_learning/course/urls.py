from django.urls import path
from course import views
from django.contrib.auth import views as v

urlpatterns = [
    path('',views.visit,name="visit"),
    path('s_signup',views.s_signup,name="s_signup"),
    path('a_signup',views.a_signup,name="a_signup"),
    path('login',views.login_view,name='login'),
    path('admin_',views.admin_home,name='admin_home'),
    path('a_',views.a_home,name="a_home"),
    path('s_',views.s_home,name="s_home"),
    path('p/<int:id>',views.play,name="play"), #playing the course
	path('add',views.add,name="add"), #adding the course
	# path('a_course',views.a_course,name="a_course"), #View the list of courses of that particular author
    path('s_enroll/<int:vid>',views.s_enroll,name="s_enroll"),# Enroll the student for the course
    path('s_learning',views.s_learning,name="s_learning"), # View the list of enrolled courses of that particular student
    path('logout/',v.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('a_t_s',views.admin_teacher_status,name="admin_teacher_status"),
    path('a_c_s',views.admin_course_status,name="admin_course_status"),
    path('a_accept_t_s/<int:aid>',views.accept_teacher_status,name="accept_teacher_status"),
    path('a_reject_t_s/<int:aid>',views.reject_teacher_status,name="reject_teacher_status"),
    path('a_submit_v_p/<int:aid>',views.submit_valid_proof,name="submit_valid_proof"),
    path('a_accept_v_s/<int:vid>',views.accept_course_status,name="accept_course_status"),
    path('a_reject_v_s/<int:vid>',views.reject_course_status,name="reject_course_status"),
    path('a_rejected_v/<int:vid>',views.video_rejected,name="video_rejected"),
    path('a_remove_v/<int:vid>',views.remove_video,name="remove"),
    
    
]
