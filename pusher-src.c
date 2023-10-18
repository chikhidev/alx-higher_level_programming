#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]) {
    if (argc < 4) {
        printf("Usage: %s <file1> <file2> ... <fileN> <commit_message>\n", argv[0]);
        return 1;
    }

    char git_add_command[1024] = "git add ";
    for (int i = 1; i < argc - 1; i++) {
        strcat(git_add_command, argv[i]);
        if (i < argc - 2) {
            strcat(git_add_command, " ");
        }
    }

    if (system(git_add_command) != 0) {
        printf("Failed to execute 'git add'. Check if Git is installed and the file paths are correct.\n");
        return 1;
    }

    char git_commit_command[1024] = "git commit -m '";
    strcat(git_commit_command, argv[argc - 1]);
    strcat(git_commit_command, "'");

    if (system(git_commit_command) != 0) {
        printf("Failed to execute 'git commit'. Make sure you have changes to commit.\n");
        return 1;
    }

    if (system("git push") != 0) {
        printf("Failed to execute 'git push'. Make sure you have configured a remote repository.\n");
        return 1;
    }

    printf("Git add, commit, and push successful.\n");

    return 0;
}

