from rest_framework import permissions

from main.permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerySetMixin:
    user_field = "user"
    allow_staff = True

    def get_queryset(self, *args, **kwargs):
        lookup_data = {self.user_field: self.request.user}
        qs = super().get_queryset(*args, **kwargs)
        if self.request.user.is_staff and self.allow_staff:
            return qs
        return qs.filter(**lookup_data)
