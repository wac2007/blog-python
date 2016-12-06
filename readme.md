Adicione no seu .git/hooks/post-commit
```pelican content -o output -s pelicanconf.py && ghp-import output && git push origin gh-pages```
