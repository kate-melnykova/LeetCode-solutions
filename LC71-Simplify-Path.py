"""
Given a string path, which is an absolute path (starting with a slash '/')
to a file or directory in a Unix-style file system, convert it to the
simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory,
a double period '..' refers to the directory up a level, and any multiple
consecutive slashes (i.e. '//') are treated as a single slash '/'. For
this problem, any other format of periods such as '...' are treated as
file/directory names.

The canonical path should have the following format:
(*) The path starts with a single slash '/'.
(*) Any two directories are separated by a single slash '/'.
(*) The path does not end with a trailing '/'.
(*) The path only contains the directories on the path from the root
    directory to the target file or directory (i.e., no period '.' or
    double period '..')
(*) Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example 4:
Input: path = "/a/./b/../../c/"
Output: "/c"

Constraints:
(*) 1 <= path.length <= 3000
(*) path consists of English letters, digits, period '.', slash '/' or '_'.
(*) path is a valid absolute Unix path.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Convert path to UNIX format
        :param path: path in windows format
        :return: path in UNIX format

        Runtime complexity: O(n) (go over the path once)
        Space complexity: O(n) (for path_decomposed)
        """
        path_decomposed = []
        cur_folder = ''  # store the cur_folder name built letter by letter
        n_dots = 0
        for char in path:
            if char == '.':
                n_dots += 1
            elif char == '/' and not n_dots and not cur_folder:
                # duplicate slash
                continue
            elif char == '/' and (cur_folder or n_dots > 2):
                # there is at least one letter in the folder name or multiple dots,
                # so we have a complete folder name
                # add it to path_decomposed
                path_decomposed.append(cur_folder + '.' * n_dots)
                cur_folder = ''
                n_dots = 0
            elif char == '/' and n_dots == 2 and path_decomposed:
                # cur_folder is emtpy, so we have a pattern ../
                # go up along the path
                path_decomposed.pop()
                n_dots = 0
            elif char == '/':
                # at all other cases when we meet '/', do nothing, reset n_dots and current_folder
                n_dots = 0
                cur_folder = ''
            else:
                # char != '.' and char != '/', so it is a letter or _
                # add a character, but take into account potential dots
                cur_folder += '.' * n_dots + char
                n_dots = 0
        # process the last folder
        if cur_folder or n_dots > 2:
            path_decomposed.append(cur_folder + '.' * n_dots)
        elif n_dots == 2 and path_decomposed:
            path_decomposed.pop()

        return '/' + '/'.join(path_decomposed)


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        ["/home/", "/home"],
        ["/../", "/"],
        ["/home//foo/", "/home/foo"],
        ["/a/./b/../../c/", "/c"],
        ["/./../.../", "/..."],
        ["/.c/..a/a./.ba.././", "/.c/..a/a./.ba.."]
    ]
    print(f'Running tests for simplifyPath')
    run_tests(Solution().simplifyPath, correct_answers)