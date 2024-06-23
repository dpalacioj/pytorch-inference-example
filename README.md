### pytorch-inference-example

### Software And Tools Requierements

1. [Github Account](https://github.com)
2. [VSCodeIDE](https://code.visualstudio.com/)

Create a new environment using conda (it could be optional)

```
conda create --name ml_env python==3.10 -y
```

Then is necesary to install de requirements as following:
```
pip install -r requirements.txt
```

Unit test: These were made using ```Pytest```

1. Verify an empy tensor</br>
2. Verify negative tensors</br>
3. Verify inference


To verify locally the docker you have to execute the following in the terminal:

```docker run -p 8000:8000 pytorch-inference-api```

The result is something like this:
```
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
To access to the API:

```http://localhost:8000/docs```

To deploy it using AWS:

First, we have to create a ECR - Elastic Container Registry. You can hold the default configuration, and after this you just need copy the URI:
```730335656576.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference-api```

