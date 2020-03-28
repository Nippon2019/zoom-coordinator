import git
    
repo = git.Repo(search_parent_directories=True)
commit = repo.head.object.hexsha
