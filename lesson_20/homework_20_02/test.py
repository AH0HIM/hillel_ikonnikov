import subprocess

result = subprocess.run('IPCONFIG',
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        encoding='windows-1251')

print(result.stdout)




"""
git status
-- if untracked files 

git add .





"""