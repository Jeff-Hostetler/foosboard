# Foosboard

Fooboard is a bare-bones app to track foosball scores.

## Setting up for Development

To start the Foosboard app locally, you will need to create a postgres database:

```
createdb foosboard
```

Next, connect to the databse and run all the SQL in `schema.sql`.

```
psql -d foosboard
````

Make sure there are the following environment variables set.

```
export DATABASE_URL="postgres://[your db username]@localhost/foosboard"
export APP_SETTINGS="config.DevelopmentConfig"
```

Finally, start the server.

```
python server.py
```
