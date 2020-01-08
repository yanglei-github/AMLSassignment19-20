# AMLSassignment19_20
**Caution:** 

The Repository in Github is only used for evidence that how I gradually built and tested my solution. SO I don't put datasets and other things in Github, the whole project you can find in the link of Google Drive(https://drive.google.com/file/d/1t0iQqDUBqeIoaRB84S8ekfAf490LXkpS). **You must use the link of google drive to access my project and run my code in google drive, which can be run successfully**.(Because the Github repository name is  *AMLSassignment19_20*, which is asked in your assignment submission description part, but in Code criteria description part, you asked to use *AMLS_19-20_Lei_Yang_SN19041732* as the folder name. It will cause the directory name in my code is different in google drive and github. **So you have to run my whole project in google drive, not the project in Github**)

This is the AMLS assignment project, which contains four models and the two datasets(celeb,cartoon_set) we used. The dataset celeb is a sub-set of a celebrity image dataset(*S. Yang, P. Luo, C. C. Loy, and X. Tang, "From facial parts responses to face detection: A Deep Learning Approach", in IEEE International Conference on Computer Vision (ICCV), 2015*). And the dataset cartoon_set is a sub-set of Cartoon Set, which could be found in *https://google.github.io/cartoonset/*.

The code of four tasks are encapsulated as four modules in their folders(A1,A2,B1,B2). In main.py, you can easily import these four model, for example, by using code 'import A1'.

The following packages are required to run my code:

numpy, pandas,  matplotlib.pyplot，PIL, cv2, sklearn(sklearn.model_selection, sklearn.preprocessing, sklearn.decomposition, sklearn.metrics, sklearn.pipeline, sklearn.linear_model), time



Note:

1. Highly recommend for using Pycharm to open the whole project(Pycharm can automatically detect the path of my module A1,A2,B1,B2 in my project).

2. In Pycharm, when you run this main.py for the first time, you have to select the Script path of main.py to run it. 

   Script path example : 'your current position(such as D:\\)' + 'AMLS_19-20_Lei_Yang_SN19041732\main.py' Also, you have to make sure that your Working directory is 'AMLS_19-20_Lei_Yang_SN19041732', which path is 'your current position(such as D:\\)' + 'AMLS_19-20_Lei_Yang_SN19041732', for example, 'D:\\AMLS_19-20_Lei_Yang_SN19041732'.

   In Pycharm, it is easy to do the configuration talked above.

   Steps as follows:

   - In the Configuration tab of Pycharm:  click edit configuration button. From the Script path name list select a type of target to run. Then, in the corresponding field, specify the path to the Python script to be executed.
