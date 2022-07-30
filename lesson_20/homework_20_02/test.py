import subprocess
from enum import Enum
from loguru import logger




changes = 'Changes to be committed'
message = 'innit'
branch = 'origin/master'


class ResultCode(Enum):
    OK = 0
    ERROR = 1


class GitCommand(Enum):
    STATUS = 'git status asd'
    ADD = 'git add .'
    COMMIT = 'git commit -m {}'
    PUSH = 'git push {}'


def git_commit():
    status_result = subprocess.run(GitCommand.STATUS.value,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   encoding='windows-1251')

    if status_result.returncode == ResultCode.ERROR.value:
        # print(status_result.stdout + status_result.stderr)
        # print('Something wrong')
        logger.error(status_result.stdout + status_result.stderr)
    else:
        if status_result.stdout.find(changes):
            print(status_result.stdout)
            add_result = subprocess.call(GitCommand.ADD.value)
            if status_result.returncode == ResultCode.ERROR.value:
                print(status_result.stdout + status_result.stderr)
                print('Something wrong')
            else:
                commit_result = subprocess.run(GitCommand.COMMIT.value.format(message),
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE,
                                               encoding='windows-1251')
                if status_result.returncode == ResultCode.ERROR.value:
                    print(status_result.stdout + status_result.stderr)
                    print('Something wrong')

                else:
                    push_result = subprocess.run(GitCommand.PUSH.value.format(branch),
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE,
                                                 encoding='windows-1251')

        else:
            print("Nothing to commit")


git_commit()

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
