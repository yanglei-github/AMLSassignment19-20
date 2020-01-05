import A1
import A2
import B1
import B2

# ======================================================================================================================
# Task A1
model_A1 = A1.A1() # Build model object.
data_train, data_val, data_test = model_A1.data_preprocessing('./Datasets/celeba/labels.csv','./Datasets/celeba/img/')
acc_A1_train = model_A1.train(data_train[0],data_train[2]) # Train model based on the training set (you should fine-tune your model based on validation set.)
acc_A1_test = model_A1.test(data_test[0],data_test[1])  # Test model based on the test set.

#the learning curve graph can be shown by running the following code(call the function 'plot_of_learningcurve')
#Notation: when you run the following code, you have to manually close the graph to make our whole code to continue to run.
#model_A1.plot_of_learningcurve(data_train[0],data_train[2])


# ======================================================================================================================
# Task A2
model_A2 = A2.A2() # Build model object.
data_train, data_val, data_test = model_A2.data_preprocessing('./Datasets/celeba/labels.csv','./Datasets/celeba/img/')
acc_A2_train = model_A2.train(data_train[0],data_train[2]) # Train model based on the training set (you should fine-tune your model based on validation set.)
acc_A2_test = model_A2.test(data_test[0],data_test[1])  # Test model based on the test set.

#the learning curve graph can be shown by running the following code(call the function 'plot_of_learningcurve')
#Notation: when you run the following code, you have to manually close the graph to make our whole code to continue to run.
#model_A2.plot_of_learningcurve(data_train[0],data_train[2])


# ======================================================================================================================
# Task B1
model_B1 = B1.B1()
data_train, data_val, data_test = model_B1.data_preprocessing('./Datasets/cartoon_set/labels.csv','./Datasets/cartoon_set/img/')
acc_B1_train = model_B1.train(data_train[0],data_train[2]) # Train model based on the training set (you should fine-tune your model based on validation set.)
acc_B1_test = model_B1.test(data_test[0],data_test[1])  # Test model based on the test set.

#the learning curve graph can be shown by running the following code(call the function 'plot_of_learningcurve')
#Notation: when you run the following code, you have to manually close the graph to make our whole code to continue to run.
#model_B1.plot_of_learningcurve(data_train[0],data_train[2])


# ======================================================================================================================
# Task B2
model_B2 = B2.B2()
data_train, data_val, data_test = model_B2.data_preprocessing('./Datasets/cartoon_set/labels.csv','./Datasets/cartoon_set/img/')
acc_B2_train = model_B2.train(data_train[0],data_train[2]) # Train model based on the training set (you should fine-tune your model based on validation set.)
acc_B2_test = model_B2.test(data_test[0],data_test[1])  # Test model based on the test set.

#the learning curve graph can be shown by running the following code(call the function 'plot_of_learningcurve')
#Notation: when you run the following code, you have to manually close the graph to make our whole code to continue to run.
#model_B2.plot_of_learningcurve(data_train[0],data_train[2])

# ======================================================================================================================
## Print out results:
print('TA1:{},{};TA2:{},{};TB1:{},{};TB2:{},{};'.format(acc_A1_train, acc_A1_test,
                                                        acc_A2_train, acc_A2_test,
                                                        acc_B1_train, acc_B1_test,
                                                        acc_B2_train, acc_B2_test))





