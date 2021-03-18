import pandas as pd
import os
import shutil

#create a data for positive samples
file_path = "covid-chestxray-dataset-master/metadata.csv"
image_path = "covid-chestxray-dataset-master/images"
df = pd.read_csv(file_path)
print(df.shape)
df.head()


test_target_dir ="dataset/test/covid"
if not os.path.exists(test_target_dir):
  os.mkdir(test_target_dir)
  print("created")
  
  
val_target_dir ="dataset/train/covid"
if not os.path.exists(val_target_dir):
  os.mkdir(val_target_dir)
  print("created")
  
  
  
  
cnt=0
for (i,row) in df.iterrows():
  if row["finding"] == "Pneumonia/Viral/COVID-19" and row["view"]=="PA":
    if (cnt<158):
      filename = row["filename"]
      Image_path = os.path.join(image_path,filename)
      image_copy_path = os.path.join(val_target_dir,filename)
      shutil.copy2(Image_path,image_copy_path)
      print("Moving image ",cnt)
    else:
      filename = row["filename"]
      Image_path = os.path.join(image_path,filename)
      image_copy_path = os.path.join(test_target_dir,filename)
      shutil.copy2(Image_path,image_copy_path)
      print("Moving test image ",cnt)
    cnt+=1
print(cnt)




import random
kaggle_file_path = "/content/chest_xray/train/NORMAL"
test_target_normal_path = "dataset/test/normal" 
val_target_normal_path = "dataset/train/normal"




image_names = os.listdir(kaggle_file_path)
random.shuffle(image_names)

for i in range(196):
  if (i<158):
    image_name =image_names[i]
    image_path = os.path.join(kaggle_file_path,image_name)

    target_path = os.path.join(val_target_normal_path,image_name)
    shutil.copy2(image_path, target_path) 
    print("Copying image ",i)
  else:
    image_name =image_names[i]
    image_path = os.path.join(kaggle_file_path,image_name)

    target_path = os.path.join(test_target_normal_path,image_name)
    shutil.copy2(image_path, target_path) 
    print("Copying test image ",i)
    
train_path = "/content/dataset/train"
val_path = "/content/dataset/test"




import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.layers import *
from keras.models import *
from keras.preprocessing import image


#cnn based model in keras

model = Sequential()
model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=(224,224,3)))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(128,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss=keras.losses.binary_crossentropy, optimizer='adam', metrics=['accuracy'])




#train from scratch

train_datagen = image.ImageDataGenerator(
    rescale=1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip=True
)

test_dataset = image.ImageDataGenerator(rescale=1./255)





train_generator = train_datagen.flow_from_directory(
    'dataset/train',
    target_size = (224,224),
    batch_size = 32,
    class_mode = 'binary')


train_generator.class_indices



validation_generator =  test_dataset.flow_from_directory(
    'dataset/test',
    target_size = (224,224),
    batch_size = 32,
    class_mode = 'binary')


hist = model.fit(
    train_generator,
    steps_per_epoch = 10,
    epochs =10,
    validation_data = validation_generator,
    validation_steps = 2
)
