from github import Github
import os

g = Github('TOKEN HERE')

org = g.get_organization('ORGANIZATION HERE')

clone_dir = './ORGANIZATION_NAME'


for repo in org.get_repos():
    
    print('Cloning', repo.name)
    ssh_url = repo.ssh_url

    list = ssh_url.split(":")
    list.insert(1, '-SSH_NAME_HERE:')
    
    new_url = ''.join(list)
    
    os.system(f'git clone {new_url} {clone_dir}/{repo.name}')
