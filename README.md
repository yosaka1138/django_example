# django_example
Djangoの練習

[この本](https://www.shuwasystem.co.jp/book/9784798061924.html)の実装をやってる

## how to run server
SECRET_KEYを隠すために，settings.pyに書くのではなくlocal_settings.pyというファイルからimportするようにしている（これが一般的っぽい）。
local_settings.pyを生成するには，generate_secret_key.pyを以下のように実行する
```bash
$ python get_random_secret_key.py > local_settings.py
```

以上を実行したのち，Djangoサーバを起動する
```bash
$ python manage.py runserver
```
