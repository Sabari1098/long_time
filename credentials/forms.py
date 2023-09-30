# from django import forms
# from .models import Student,Courses
#
# class StudentForm(forms.ModelForm):
#     class Meta:
#         model= Student
#         fields = ('name','dob','age','gender','phone','mail','address','department','course','purpose','material')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['course'].queryset = Courses.objects.none()
#
#         if 'credentials_department' in self.data:
#             try:
#                 credentials_department_id = int(self.data.get('credentials_department'))
#                 self.fields['credentials_courses'].queryset = Courses.objects.filter(credentials_department_id=credentials_department_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['credentials_courses'].queryset = self.instance.department.course_set.order_by('name')
