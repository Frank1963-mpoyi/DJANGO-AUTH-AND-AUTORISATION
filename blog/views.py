from django.contrib                                     import messages
from django.contrib.auth.mixins                         import LoginRequiredMixin
from django.shortcuts                                   import render, redirect
from django.urls                                        import reverse_lazy
from django.views.generic                               import View

from common                                             import user  as user_common
from .forms             import IssueCreateForm
from .input             import input_get_input, input_post_input
from common.email                                import SRIssueNotificationEmail
# from .lib                                               import issue as issue_lib


# Create your views here.
class IssueCreateView(LoginRequiredMixin, View):
    template_name = 'blog/issues.html'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        form = IssueCreateForm(request.POST or None)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        staff = user_common.check_allowed_staff(self)

        context = {
            'i'         : i,
            'page_name' : 'issues',
            'action'    : 'create',
            'form'      : form,
            'staff'     : staff,
            # 'country'       : ip_data.get('country'),
        }

        return render(request, self.template_name, context)

    def post(self, request, **kwargs):

        i = input_post_input(self)

        form = IssueCreateForm(request.POST or None)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        staff = user_common.check_allowed_staff(self)

        issue = issue_lib.create_issue(i, staff)

        if issue:

            SRIssueNotificationEmail(issue, ip_data, i=i).start()

            messages.success(request, "Issue successfully created.")

            return redirect(reverse_lazy('web:issues:list') + '')

        messages.warning(request, "Issue not saved. Please try again.")

        context = {
            'i'         : i,
            'page_name' : 'issues',
            'action'    : 'create',
            'form'      : form,
            'staff'     : staff,
            # 'country'       : ip_data.get('country'),
        }

        return redirect(self.request.META['HTTP_REFERER'])


# Create your views here.
