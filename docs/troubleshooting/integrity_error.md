# Integrity Error

Example:  

```plaintext
IntegrityError at /admin/auth/user/
update or delete on table "auth_user" violates foreign key constraint "practice_v1_profile_user_id_f945ebf2_fk_auth_user_id" on table "practice_v1_profile"
DETAIL:  Key (id)=(6) is still referenced from table "practice_v1_profile".
Request Method:	POST
Request URL:	http://localhost:8000/admin/auth/user/
Django Version:	3.2.14
Exception Type:	IntegrityError
Exception Value:	
update or delete on table "auth_user" violates foreign key constraint "practice_v1_profile_user_id_f945ebf2_fk_auth_user_id" on table "practice_v1_profile"
DETAIL:  Key (id)=(6) is still referenced from table "practice_v1_profile".
Exception Location:	/usr/local/lib/python3.10/site-packages/django/db/backends/base/base.py, line 242, in _commit
Python Executable:	/usr/local/bin/python
Python Version:	3.10.2
Python Path:	
['/code',
 '/usr/local/lib/python310.zip',
 '/usr/local/lib/python3.10',
 '/usr/local/lib/python3.10/lib-dynload',
 '/usr/local/lib/python3.10/site-packages']
Server time:	Fri, 26 Aug 2022 12:07:04 +0000
```

User を削除しようとしたあとに起こる  

`practice_v1` は `practice_vol1o0` に名前変更したが、関係あるか？  

データベースをクリアーするには？  

📖 [What is the easiest way to clear a database from the CLI with manage.py in Django?](https://stackoverflow.com/questions/6485106/what-is-the-easiest-way-to-clear-a-database-from-the-cli-with-manage-py-in-djang)  

Input:  

```shell
docker-compose run --rm web python manage.py flush
```

Output:  

```plaintext
CommandError: Database postgres couldn't be flushed. Possible reasons:
  * The database isn't running or isn't configured correctly.
  * At least one of the expected database tables doesn't exist.
  * The SQL was invalid.
Hint: Look at the output of 'django-admin sqlflush'. That's the SQL this command wasn't able to run.
ERROR: 1
```

Input:  

```shell
docker-compose run --rm web python manage.py reset practice_vol1o0
#                                                  ---------------
#                                                  1
# 1. アプリケーション
```

Output:  

```plaintext
Unknown command: 'reset'. Did you mean test?
Type 'manage.py help' for usage.
ERROR: 1
```
