import {EDITABLE_PRP_ROLES, PRP_ROLE, USER_TYPE} from "../constants";
import {getUserRole, hasAnyRole, hasOnlyRoles, userRoleInWorkspace} from "./user";
import * as R from 'ramda';
import {PORTALS} from "../actions";

const isSystemAdmin = (user) => hasAnyRole(user, [PRP_ROLE.CLUSTER_SYSTEM_ADMIN]);

const _permissions = {
    addUserPermission: ({userProfile}, user) => (
        user.status !== "DEACTIVATED" &&
        user.user_type !== USER_TYPE.CLUSTER_ADMIN &&
        hasAnyRole(userProfile, [
            PRP_ROLE.IP_ADMIN,
            PRP_ROLE.IP_AUTHORIZED_OFFICER,
            PRP_ROLE.CLUSTER_IMO,
            PRP_ROLE.CLUSTER_MEMBER,
            PRP_ROLE.CLUSTER_SYSTEM_ADMIN,
        ])
    ),
    editUserPermission: ({userProfile, portal}, permission, user) => {
        const userRole = getUserRole(userProfile, permission, portal);

        switch (userRole) {
            case PRP_ROLE.IP_ADMIN:
            case PRP_ROLE.CLUSTER_IMO:
            case PRP_ROLE.CLUSTER_MEMBER:
            case PRP_ROLE.CLUSTER_SYSTEM_ADMIN:
                return user.status !== "DEACTIVATED" && EDITABLE_PRP_ROLES[userRole].indexOf(permission.role) > -1;
            default:
                return false;
        }
    },
    makeSystemAdmin: ({userProfile}, user) => isSystemAdmin(userProfile) && !isSystemAdmin(user),
    makeIpAdmin: ({userProfile, portal}, permission) => {
        const userRole = getUserRole(userProfile, permission, portal);

        return userRole === PRP_ROLE.IP_AUTHORIZED_OFFICER &&
            ([PRP_ROLE.IP_EDITOR, PRP_ROLE.IP_VIEWER].indexOf(permission.role) > -1);
    },
    revokeIpAdmin: ({userProfile, portal}, permission) => {
        const userRole = getUserRole(userProfile, permission, portal);

        return userRole === PRP_ROLE.IP_AUTHORIZED_OFFICER &&
            permission.role === PRP_ROLE.IP_ADMIN;
    },
    deleteUser: ({userProfile}, user) => {
        let hasIpAdmin = true;

        user.prp_roles.forEach(role => {
            if (!role.workspace || userRoleInWorkspace(userProfile, role.workspace.id) !== PRP_ROLE.IP_ADMIN) {
                hasIpAdmin = false;
            }
        });

        return hasIpAdmin && hasOnlyRoles(user, [PRP_ROLE.IP_EDITOR, PRP_ROLE.IP_VIEWER])
    },
    filterPartners: [
        PRP_ROLE.CLUSTER_SYSTEM_ADMIN,
        PRP_ROLE.CLUSTER_IMO
    ],
    manageUser: ({userProfile, portal}) => hasAnyRole(userProfile, [PRP_ROLE.IP_ADMIN]) && portal === PORTALS.IP
};

export function computePermissions(state) {
    const params = {
        userProfile: state.user,
        portal: state.portal
    };

    return R.map(granted => {
        switch (true) {
            case Array.isArray(granted):
                return hasAnyRole(params.userProfile, granted);

            case typeof granted === "function":
                return function () {
                    const args = [].slice.call(arguments);

                    const fn = granted.apply(null, [params].concat(args));

                    return args.length ? fn : fn();
                };

            default:
                return false;
        }
    }, _permissions);
}

