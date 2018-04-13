#!/usr/bin/env bash

ex -sc '%s/{REPOSITORY_USER_NAME}/'"$REPOSITORY_USER_NAME"'/g' -cx settings.xml
ex -sc '%s/{JFROG_USERNAME}/'"$JFROG_USERNAME"'/g' -cx settings.xml
ex -sc '%s/{REPOSITORY_PASSWORD}/'"$REPOSITORY_PASSWORD"'/g' -cx settings.xml
ex -sc '%s/{JFROG_KEY}/'"$JFROG_KEY"'/g' -cx settings.xml