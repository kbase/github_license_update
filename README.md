
## Adds `LICENSE` files to repos programattically

This is a quick little tool to add `LICENSE.md` files to a list of GitHub repos.

### Dependencies

- Python 3
- [pyyaml](https://pypi.org/project/PyYAML/)
- [pygithub](https://pypi.org/project/PyGithub/)

### Usage

1. Install required dependencies (listed above)
2. Update `config.yaml` with:
    - Your GitHub [access token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)
    - A list of repos to be updated. This should be a single-line `.csv` with the format `user/repo` or `org/repo`
    - The license file you wish to add to each repo
3. Run the script with `python update_license.py`

### Potential Improvements

- Simplify installation with a `setuptools`-based `setup.py`
- Ability to poll an entire org, and add a `LICENSE` to any repo that lacks one
- Multi-license support, using two columns in the `repo_file`: 
    - Repo
    - License type
- Ability to update existing repos if they aren't using the latest version of their respective licenses