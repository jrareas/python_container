**RUN it locally**

The command below from the root folder will build the base docker and up

`make build-base`

The command below will push base to the repo

`make push-base`

This will change though

**DEBUG**
make sure the map is set in your yaml file. Example:

`- PATHS_FROM_ECLIPSE_TO_PYTHON=[["/Users/jareas/Developer/ja-docker-images/python_container/docker/base","/app"]]`

***Migrations**
from the root folder run

Creating:

`alembic revision -m "create account table"`

running:


`alembic -c development.ini upgrade head`

Rollback to Scratch:

`alembic -c development.ini downgrade base`
