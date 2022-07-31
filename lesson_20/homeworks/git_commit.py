import subprocess
import argparse
from dataclasses import dataclass
from enum import Enum

from loguru import logger

logger.add("logs/logs.log", format="{time} {level} {message}", level="DEBUG", rotation="10 KB")
logger.info("Changes to be committed")
logger.error("Something wrong")


@dataclass(frozen=True)
class GitCommands:
    status = 'git status'
    add = 'git add .'
    commit = 'git commit -m {}'
    push = 'git push {}'


class ExitCodes(Enum):
    OK = 0
    ERROR = 1


class GitClass:

    def __init__(self, message, branch):
        self.message = message
        self.branch = branch

    def git_status(self):
        status_result = subprocess.run(GitCommands.status,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       encoding='windows-1251')

        if status_result.returncode == ExitCodes.ERROR:
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
        add_result = subprocess.run(GitCommands.add,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    encoding='windows-1251')
        if add_result.returncode == ExitCodes.ERROR:
            logger.error(add_result.stdout + add_result.stderr)
            return

        else:
            logger.info(add_result.stdout)
            self.git_commit()

    def git_commit(self):
        commit_result = subprocess.run(GitCommands.commit.format(self.message),
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       encoding='windows-1251')
        if commit_result.returncode == ExitCodes.ERROR:
            logger.error(commit_result.stdout + commit_result.stderr)
            return

        else:
            logger.info(commit_result.stdout)
            self.git_push()

    def git_push(self):
        push_result = subprocess.run(GitCommands.push.format(self.branch),
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     encoding='windows-1251')
        if push_result.returncode == ExitCodes.ERROR:
            logger.error(push_result.stdout + push_result.stderr)
            return


parser = argparse.ArgumentParser()
parser.add_argument("-m", "--message", type=str, required=True, help="Enter a commit message")
parser.add_argument("-b", "--branch", type=str, help="Enter a branch", default="origin/main")

args = parser.parse_args()

if __name__ == '__main__':
    git_run = GitClass(args.message, args.branch)
    git_run.git_status()
