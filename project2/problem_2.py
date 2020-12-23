import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    current_path = list(map(lambda x: "{}/{}".format(path, x), os.listdir(path)))

    files = []
    for item in current_path:
        if os.path.isdir(item):
            files.extend(find_files(suffix, item))
        elif os.path.isfile(item):
            if item.endswith(suffix):
                files.append(item)
        else:
            pass
    return files


def testing(expected, actual):
    print("Pass" if expected == actual else "Fail : {} but {}".format(expected, actual))


def main():
    testing('./testdir/subdir1/a.c' in find_files('.c', '.'), True)
    testing('./testdir/subdir5/a.c' in find_files('.c', '.'), True)
    testing('./testdir/subdir5/a.h' in find_files('.c', '.'), False)
    testing('./testdir/subdir5/a.h' in find_files('.h', '.'), True)
    testing('./testdir/subdir3/subsubdir1/b.h' in find_files('.h', '.'), True)
    testing('./testdir' in find_files('.c', '.'), False)


main()
