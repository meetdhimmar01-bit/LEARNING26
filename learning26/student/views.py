from django.shortcuts import render


# Create your views here.
 
def studentHome(request):
    return render(request,"student/studenthome.html")

def studentDashboard(request):
    student = {"name":"meet","age":21,"city":"bilimora"}
    return render(request,"student/student_dashboard.html",student)


