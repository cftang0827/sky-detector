# sky-detector
A non-deep learning sky detector method with simple python script

### Intro
This project use very simple algorithm, we assume that the variance of sky is smaller than non-sky part. Therefore, we use `Laplacian filter` to extract the part that variance is lower than threshold.

After we extract the mask after filtering out non-sky part, then we examine every single skyline, and find out the starting point that is non-sky part. 

This method was inspired by the papaer [`Sky Region Detection in a Single Image for Autonomous Ground Robot Navigation`](https://journals.sagepub.com/doi/full/10.5772/56884)

### Requirements
```
opencv-python = "^4.2.0"
scipy = "^1.5.0"
numpy = "^1.19.0"
```

### Run the test
```bash
poetry shell # We use poetry to run the whole script, install dependencies
python test.py
```


