import git

repo = git.Repo(search_parent_directories=True)
number_of_commits = repo.head.object.hexsha
last_commit = GET /repos/:owner/:repo/commits/master

Number of commits: {{ number_of_commits }} 
Last commit: {{ last_commit }}
