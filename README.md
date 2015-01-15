# Foosboard

To start the Foosboard app locally, you will need to create a postgres database:

```
createdb foosboard
```

Next, connect to the databse and run all the SQL in `schema.sql`.

```
psql -d foosboard
````

Finally, start the server with a `DATABASE_URL` pointing to your development database:

```
DATABASE_URL=postgres://myuser@localhost/foosboard python run_server.py
```

