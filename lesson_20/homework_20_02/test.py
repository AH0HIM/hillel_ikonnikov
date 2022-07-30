import subprocess


def git_commit():
    result = subprocess.run('git status',
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding='windows-1251')

    if result.returncode == 0:
        print(result.stdout)
        print('OK')
    else:
        print(result.stdout + result.stderr)
        print('Something wrong')


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

"""
