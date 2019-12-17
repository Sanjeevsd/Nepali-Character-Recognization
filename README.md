# Nepali-Character-Recognizatio
CNN model to recognize Nepali characters
Built Using DHCD_Dataset from ** datasets and CNN model to recognize Handwritten devnagari characters.
The data set contains 46 characters(46 class) with each having 1700 train and 300test data.
The CNN model is bult using relu and softmax activation functions.The input shape is 32*32( same as the size of train datasets).Model is compiled using 'adam' optimizer and only one etrice (accuracy).
  The datasets were fed to the model by using imageGenerator and then training was done with 3epoch, each epoch is of 1500steps per epoch and validation steps of 12.(took 30min i5-5th gen 8gb ddr3lram). The resultin Sccuracy is 93.75%
 
  
  ![GitHub Logo](/screenshots/accuracy.png)
  
  The trained model was used with flask webframework for realtime character recognization.
  ![GitHub Logo](/screenshots/ka.png)
  ![GitHub Logo](/screenshots/angg.png)
  
