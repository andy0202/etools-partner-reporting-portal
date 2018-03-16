from rest_framework.permissions import BasePermission

from .models import (
    PartnerAuthorizedOfficerRole,
    PartnerEditorRole,
    IMORole
)


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        # we can extend permissions verification in future!
        return request.user.is_authenticated()


class IsPartnerAuthorizedOfficer(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated() and \
            user.groups.filter(
            name=PartnerAuthorizedOfficerRole.as_group().name).exists()


class IsPartnerEditor(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated() and \
            user.groups.filter(
            name=PartnerEditorRole.as_group().name).exists()


class IsPartnerEditorOrPartnerAuthorizedOfficer(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated() and (
            user.groups.filter(
                name=PartnerEditorRole.as_group().name).exists() or
            user.groups.filter(
                name=PartnerAuthorizedOfficerRole.as_group().name).exists()
        )


class IsIMO(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated() and user.groups.filter(name=IMORole.as_group().name).exists()


class IsIMOForCurrentWorkspace(IsAuthenticated):

    def has_permission(self, request, view):
        if super(IsIMOForCurrentWorkspace, self).has_permission(request, view):
            rules = [
                request.user.groups.filter(name=IMORole.as_group().name).exists()
            ]
            workspace_id = request.resolver_match.kwargs.get('workspace_id')
            if workspace_id:
                rules.append(
                    request.user.workspaces.filter(id=workspace_id).exists()
                )
            return all(rules)

        return False
