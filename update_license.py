import yaml
from github import Github

## Load config
with open('config.yaml') as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)

## Load list of repos and desired license file from `config.yaml`
with open(config['license_file'], 'r') as license_file:
  license = license_file.read()

with open(config['repo_file']) as repo_list:
    repos = repo_list.readlines()
repos = [x.strip() for x in repos]


## Log in, using access token defined in `config.yaml`
g = Github(config['token'])

## Attempt to upload a new `LICENSE.md` file, as defined in `config.yaml`
for current_repo in repos:
    repo = g.get_repo(current_repo)
    print("- Adding LICENSE to {0}".format(current_repo))
    try:
        repo.create_file("LICENSE.md", "Adding `LICENSE`", license, branch="master")
        print("\t Done!")
    except:
        print("\t Unable to create LICENSE in {0}".format(current_repo))
