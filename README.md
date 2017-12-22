## CloudFoundry Example Application:  Python Flask

This is an example application which can be run on CloudFoundry.
Every time when you will have an access to the application with browser, application will show users access time.


### Usage

1. Login to CF

  ```bash
  cf login -a https://api.run.pivotal.io
  ```

2. Clone the app (i.e. this repo).

  ```bash
  git clone https://github.com/vyrodovalexey/cf-flask-ex.git
  cd cf-flask-ex
  ```

3. Push it to CloudFoundry.

  ```bash
  cf push
  ```

## Enjoy!

