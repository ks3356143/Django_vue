from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET','HEAD','OPTIONS')

class IsStaffUser(BasePermission):
    #允许工作人员以及超级用户进入,has_permission是在BasePermission类中方法
    def has_permission(self,request,view):
        return bool(request.user and
                    request.user.is_staff or
                    request.user.is_superuser)

class IsStaffUserReadOnly(BasePermission):
    #该请求作为工作人员或超级用户进行身份验证，或者是只读请求
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff or
            request.user.is_superuser
        )

class IsSuperUser(BasePermission):
    """
    只允许超级用户的权限，单独权限，其他无权查看
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class IsSuperUserOrReadOnly(BasePermission):
    """
    请求允许超级用户，其他只能only-read
    """
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_superuser
        )