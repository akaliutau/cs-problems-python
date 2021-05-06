"""   We will represent the file system as a string where "\n\t" mean a
   subdirectory of the main directory, "\n\t\t" means a subdirectory of the
   subdirectory of the main directory and so on. Each folder will be represented
   as a string of letters and/or digits. Each file will be in the form "s1.s2"
   where s1 and s2 are strings of letters and/or digits. For example, the file
   system above is represented as
   "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext".
   Given a string input representing the file system in the explained format,
   return the length of the longest absolute path to a file in the abstracted
   file system. If there is no file in the system, return 0. Input: input =
   "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" Output: 20 Explanation: We have
   only one file and its path is "dir/subdir2/file.ext" of length 20. The path
   "dir/subdir1" doesn't contain any files.
"""

class Solution388:
    pass
