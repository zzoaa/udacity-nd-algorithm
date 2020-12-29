class GroupTable(object):
    def __init__(self):
        self.table = {}

    def is_user_in_group(self, user, target):
        if user in self.table:
            group_name = self.table[user]
            if group_name == target:
                return True
            else:
                return self.is_user_in_group(group_name, target)
        else:
            return False

    def append(self, child, parent):
        self.table[child] = parent


class Group(object):
    def __init__(self, _name, _group_table):
        self.name = _name
        self.groups = []
        self.users = []
        self.group_table = _group_table

    def add_group(self, group):
        self.groups.append(group)
        self.group_table.append(group.get_name(), self.name)

    def add_user(self, user):
        self.users.append(user)
        self.group_table.append(user, self.name)

    def get_group_table(self):
        return self.group_table

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    group_table = group.get_group_table()
    return group_table.is_user_in_group(user, group.get_name())


def test(expected, actual):
    print("Pass" if expected == actual else "Fail : expected [{}], but [{}]".format(expected, actual))


def main():
    table = GroupTable()

    parent = Group("parent", table)
    child = Group("child", table)
    sub_child = Group("subchild", table)

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    test(is_user_in_group(user="sub_child_user", group=sub_child), True)
    test(is_user_in_group(user="not_sub_child_user", group=sub_child), False)

    child.add_group(sub_child)

    test(is_user_in_group(user="sub_child_user", group=child), True)
    test(is_user_in_group(user="not_sub_child_user", group=child), False)

    parent.add_group(child)

    test(is_user_in_group(user="sub_child_user", group=parent), True)
    test(is_user_in_group(user="not_sub_child_user", group=parent), False)


main()
