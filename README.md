### Details
I made a web app using Flask as backend which takes in image as an input and returns the most similar images to it in the dataset taken along with the similarity score. Image feature extraction of dataset images and the user query image was done using Image histogram method in OpenCV. 

### Instructions to Run:
In terminal type
```
python runner.py
```
Open localhost:5000 in a browser

### Dataset
Comprised of multiple images in 3 categories: mountain, sea and desert. Some images were taken not belonging to these categories for testing purposes.

### Reference
I referred to this blog post by Adrian Rosebrock for image feature extraction in OpenCV: https://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/

### Future Work
Evaluating the retrieval using Precision, Recall, F1 Score would be the next target. Image feature extraction process can be made better by using SIFT or ORB features in OpenCV.