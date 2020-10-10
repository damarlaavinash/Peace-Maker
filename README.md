# Peace-Maker
Here we propose an Emotion based music player (Peace Maker). Peace Maker is a music player which plays songs according to the emotion of the user. It aims to provide user preferred music with emotion awareness. Peace Maker is based on the idea of automating much of the interaction between the music player and its user. The training dataset which we used is Olivetti faces which contain 400 faces and its desired values or parameters.  The webcam captures the image of the user. It then extract the facial features of the user from the captured image. The training process involves initializing some random values for say smiling and not smiling of our model, predict the output with those values, then compare it with the model's prediction and then adjust the values so that they match the predictions that were made previously.  Evaluation allows the testing of the model against data that has never been seen and used for training and is meant to be representative of how the model might perform when in the real world. According to the emotion, the music will be played from the predefined directories.