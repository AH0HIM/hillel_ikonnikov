import subprocess
import argparse
from dataclasses import dataclass
from enum import Enum


# from loguru import logger
#
#
# logger.add("logs/logs.log", format="{time} {level} {message}",
#            level="DEBUG", rotation="10 KB")
#
# logger.info("Changes to be committed")
# logger.error("Something wrong")


@dataclass(frozen=True)
class GitClass:
    STATUS = 'git status'
    ADD = 'git add .'
    COMMIT = 'git commit -m {}'
    PUSH = 'git push {}'
    OK = 0
    ERROR = 1


changes = 'Changes to be committed'


# class ResultCode(Enum):
#     OK = 0
#     ERROR = 1

#
# class GitCommand(Enum):
#     STATUS = 'git status'
#     ADD = 'git add .'
#     COMMIT = 'git commit -m {}'
#     PUSH = 'git push {}'


def git_commit(commit_message, branch):
    status_result = subprocess.run(GitClass.STATUS,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   encoding='windows-1251')

    if status_result.returncode == GitClass.ERROR:
        print(status_result.stdout + status_result.stderr)

    else:
        input('add')
        if status_result.stdout.find(changes):
            print(status_result.stdout)
            add_result = subprocess.call(GitClass.ADD)
            if status_result.returncode == GitClass.ERROR:
                print('error')
            else:
                input('commit')
                commit_result = subprocess.run(GitClass.COMMIT.format(commit_message),
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE,
                                               encoding='windows-1251')
                if status_result.returncode == GitClass.ERROR:
                    print(status_result.stdout + status_result.stderr)

                else:
                    input('push')
                    push_result = subprocess.run(GitClass.PUSH.format(branch),
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE,
                                                 encoding='windows-1251')

        else:
            print("Nothing to commit")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("commit_message")
    parser.add_argument("branch")

    args = parser.parse_args()

    print(args)
    git_commit(args.commit_message, args.branch)

"""
сделать коммит на гите, 
git status
-- if untracked files 

git add .

-- if no error = ok


git commit - m '{message}'

-- if no error = ok

git status

if nothing to commit, working tree clean


git push {origin}

"""
