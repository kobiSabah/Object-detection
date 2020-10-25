## Mask detection

#### Overview:

Create your own object detection using cascade classifier - OpenCV

#### Requirements:
- OpenCv ``` pip install opencv-python ```
- 300+ Positive images (image that contain your object)
- 300+ Negative/Background (image that not contain your object)
- OpenCv annotation tool [Click here][1]

[1]: https://sourceforge.net/projects/opencvlibrary/files/3.4.12/


### Steps

*1.* Create a text file with all the negative image paths and name it _neg.txt_
It's should look like this:
```
Images/Negative/neg_11.jpg
Images/Negative/neg_12.jpg
Images/Negative/neg_13.jpg
Images/Negative/neg_14.jpg
Images/Negative/neg_15.jpg
Images/Negative/neg_16.jpeg
Images/Negative/neg_17.jpg
Images/Negative/neg_18.jpg
Images/Negative/neg_19.jpg
```

*2.* Create the positive text file.
The positive file should contain the number of objects that appear in the image and their locations.
there is a tool in OpenCV that will make the job easier

on Trminal type : (you should cd to the directory where the annotation tools)
``` opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=Images/Positive/    ```

Now you'll see a window where you can mark the location of objects in the picture [read more.][3]

[3]:http://www.willberger.org/using-opencv_annotation-program-annotate-positive-images/

After it you should get pos.txt file that look like this :
[image path] / [number of object] / [position : X Y W H] 
```
Images/Positive/mask_110.jpg 1 73 181 184 131
Images/Positive/mask_111.jpg 1 265 512 474 330
Images/Positive/mask_112.jpg 1 207 452 428 318
Images/Positive/mask_113.png 1 263 321 233 188
Images/Positive/mask_114.jpg 1 64 171 200 165
Images/Positive/mask_115.jpg 1 61 109 134 117
Images/Positive/mask_116.jpg 1 189 324 328 295
```

*3.* create a samples file 
```opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec ```

you should get pos.vec 

*4.* Now its time to train your model 
This process requires patience. You must change the values in order to get good results
``` opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 200 -numNeg 400 -numStages 12 ```

-data: where the training file will be saved 
-vec: the sample file path
-bg: the negative txt file path 
-numPos: number of a positive image for training (should be less than what you have)
-numNeg: number of a negative image for testing (for a good train it is recommended to give twice the number of numPos)

you can read more about the values [here][2]

[2]:https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html

*5.* You're done ! now you should get _cascade.xml_ file