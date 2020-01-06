# AMLSassignment19_20
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
