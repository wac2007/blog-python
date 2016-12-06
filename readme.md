Adicione no seu .git/hooks/post-commit
```pelican content -o output -s pelicanconf.py && ghp-import output && git push git@github.com:wac2007/wac2007.github.io.git gh-pages:master --force```
