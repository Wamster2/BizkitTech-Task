from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    if not args:
        return USERS

    filtered_users = []

    for user in USERS:
        include_user = True

        if "id" in args and user["id"] == args["id"]:
            include_user = True
        elif "name" in args and args["name"].lower() in user["name"].lower():
            include_user = True
        elif "age" in args and user.get("age") and int(args["age"]) - 1 <= user["age"] <= int(args["age"]) + 1:
            include_user = True
        elif "occupation" in args and args["occupation"].lower() in user["occupation"].lower():
            include_user = True
        else:
            include_user = False

        if include_user:
            filtered_users.append(user)

    return filtered_users