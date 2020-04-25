This repository contains the implementation of the REST API that provides the ICU length-of-stay estimation. It is part
of the [BlueBeds](https://devpost.com/software/bluebeds) project and it was created during the
[EUvsVirus](https://euvsvirus.org/) hackaton.

The prediction model is taken from [here](https://github.com/rachelHey/versus-virus-hack-length-of-stay-prediction).
# Setup for development
```
pip install -r requirements/dev-requirements.txt
```

# Build docker image
```
docker build -t bluebeds-prediction-api -f docker/Dockerfile .
```

# Run docker image
```
docker run -it --name bluebeds-prediction -p 80:80 bluebeds-prediction-api
```
After running it you can access the documentation in the [localhost](http://localhost:80/docs) 