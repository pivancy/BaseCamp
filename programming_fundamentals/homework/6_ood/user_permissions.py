"""
This module describes a homework related to User's permissions verification.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# This is a task for creating a proper program design to resolve the task.
# The final solution should be implemented according to all code styles, etc.
# and all provided requirements.

# You should create a classes, functions, etc. by yourself.

# As a result we should have an activity log with all the information.
# Activity log - text file.

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.page_name = None

    def set_group(self, role):
        self.role = role

    def check_permissions(self, check_name):
        self.page_name = check_name.page_name

        if self.role in check_name.roles_list:
            return True
        else:
            return False

    def login(self):
        try:
            with open('activity_log.txt', 'a') as file:
                file.write('User \'{}\' has been successfully logged in \'{}\' page.\n'
                           .format(self.name, self.page_name))
        except (OSError, IOError) as err:
            print('Could not write to file:', err)

    def logot(self):
        try:
            with open('activity_log.txt', 'a') as file:
                file.write('User \'{}\' has not enough permissions for \'{}\' page.\n'
                           .format(self.name, self.page_name))
        except (OSError, IOError) as err:
            print('Could not write to file:', err)


class Page:
    def __init__(self, page_name):
        self.page_name = page_name
        self.roles_list = []

    def allow_for(self, add_role):
        if isinstance(add_role, list):
            for item in add_role:
                if item not in self.roles_list:
                    self.roles_list.append(item)
        else:
            if add_role not in self.roles_list:
                self.roles_list.append(add_role)


admin_user = User("Pavlo", "admin")
moderation_user = User("Yura", "moderator")
regular_user = User("Max", "regular")
regular_user.set_group("moderator")

page = Page("Settings")
page.allow_for(["admin", "moderator"])

is_allowed_admin = admin_user.check_permissions(page)
if is_allowed_admin:
    # Login should write a success message into activity log.
    # It might be something similar to:
    # User `Pavlo` has been successfully logged in `Settings` page.
    admin_user.login()
else:
    # Logout should write an error message into activity log.
    # It might be something similar to:
    # User `Pavlo` has not enough permissions for `Settings` page.
    admin_user.logot()
