import subprocess
import argparse
from dataclasses import dataclass
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


def git_commit(commit_message, branch):
    status_result = subprocess.run(GitClass.status,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   encoding='windows-1251')

    if status_result.returncode == GitClass.error:
        logger.error(status_result.stdout + status_result.stderr)
        return

    else:
        input('add')
        if 'Changes not staged for commit' in status_result.stdout:
            logger.info(status_result.stdout)
            subprocess.call(GitClass.add)
            if status_result.returncode == GitClass.error:
                logger.error('error')
            else:
                input('commit')
                commit_result = subprocess.run(GitClass.commit.format(commit_message),
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE,
                                               encoding='windows-1251')
                if status_result.returncode == GitClass.error:
                    logger.error(commit_result.stdout + commit_result.stderr)

                else:
                    input('push')
                    push_result = subprocess.run(GitClass.push.format(branch),
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE,
                                                 encoding='windows-1251')
                    if status_result.returncode == GitClass.error:
                        logger.error(push_result.stdout + push_result.stderr)

        else:
            input('push2')
            push_result = subprocess.run(GitClass.push.format(branch),
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         encoding='windows-1251')
            if status_result.returncode == GitClass.error:
                logger.error(push_result.stdout + push_result.stderr)


parser = argparse.ArgumentParser()
parser.add_argument("-m", "--message", type=str, required=True, help="Enter a commit message")
parser.add_argument("-b", "--branch", type=str, help="Enter a branch", default="origin")

args = parser.parse_args()

if __name__ == '__main__':
    git_commit(args.message, args.branch)
