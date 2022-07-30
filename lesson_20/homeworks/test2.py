import subprocess
import argparse
from dataclasses import dataclass
from enum import Enum

from loguru import logger

logger.add("logs/logs.log", format="{time} {level} {message}",
           level="DEBUG", rotation="10 KB")

logger.info("Changes to be committed")
logger.error("Something wrong")


@dataclass(frozen=True)
class GitClass:
    status = 'git status'
    add = 'git add .'
    commit = 'git commit -m {}'
    push = 'git push {}'
    ok = 0
    error = 1
    committed = 'Your branch is ahead'


class GitRun:

    def __init__(self, commit_message, branch):
        self.commit_message = commit_message
        self.branch = branch

    def git_status(self):
        status_result = subprocess.run(GitClass.status,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       encoding='windows-1251')

        if status_result.returncode == GitClass.error:
            logger.error(status_result.stdout + status_result.stderr)
            return

        else:
            if 'Changes not staged for commit' in status_result.stdout:
                logger.info(status_result.stdout)
                self.git_add()
            else:
                if 'Your branch is ahead' in status_result.stdout:
                    logger.info(status_result.stdout)
                    self.git_push()
                else:
                    logger.info("Nothing to commit")
                    return

    def git_add(self):
        add_result = subprocess.run(GitClass.add,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    encoding='windows-1251')
        if add_result.returncode == GitClass.error:
            logger.error('error')
            return

        else:
            logger.info(add_result.stdout)
            self.git_commit()

    def git_commit(self):
        commit_result = subprocess.run(GitClass.commit.format(self.commit_message),
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       encoding='windows-1251')
        if commit_result.returncode == GitClass.error:
            logger.error(commit_result.stdout + commit_result.stderr)
            return

        else:
            logger.info(commit_result.stdout)
            self.git_push()

    def git_push(self):
        push_result = subprocess.run(GitClass.push.format(self.branch),
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     encoding='windows-1251')
        if push_result.returncode == GitClass.error:
            logger.error(push_result.stdout + push_result.stderr)
            return


# parser = argparse.ArgumentParser()
# parser.add_argument("-m", "--message", type=str, required=True, help="Enter a commit message")
# parser.add_argument("-b", "--branch", type=str, help="Enter a branch", default="origin")
#
# args = parser.parse_args()


if __name__ == '__main__':
    git_run = GitRun('innit', 'origin')
    git_run.git_status()
