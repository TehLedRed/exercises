# exercises

1. run:
```shell
make run
```

2. Access SonarQube: [site](https://sonarqube.docker.localhost/)
   1. Login using default credential: admin (Username) and admin (Password)
   2. Reset password
   3. Select manually
   4. Generate token and save this value to .env key `SONARQUBE_PROJECT_KEY`

3. run in a new terminal:
```shell
make sonar
```