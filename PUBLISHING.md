# Releasing a version

1. commit all changes
2. change to `main` branch
3. merge changes as needed
4. run `poetry version [rule]`
5. commit changes
6. run `git tag v$(poetry version -s)`
7. push changes
8. run `poetry publish --build`