# Smart Attendance System 

![Flowchart](https://user-images.githubusercontent.com/81853910/234709101-91fe7231-fc55-450a-8791-7536340de0f4.png)

# 📄 Documentation

Project was entirely documented through a summary-cum-logbook.

The link for document can be found [here](https://docs.google.com/document/d/1d7mIC_XObldqrMN3rBEGLxJHqO9GOloJhzTvwr5MwOo/edit?usp=sharing).

## Setup

Install Dependencies


```
pip install flask
```

```
pip install opencv-python
```


```
pip install numpy
```


To install `face_recognition`, Refer to [this video](https://youtu.be/xaDJ5xnc8dc)

**To run the project, run the `app.py` in terminal**

![Way to Run the app.py](https://user-images.githubusercontent.com/81853910/234709700-af4ec50b-f30a-4ec9-b5c3-5019b28e0c33.png)

## Steps to Add your Face in the training dataset

- Add your image in the training dataset.
- Go to [detection_engine.py](https://github.com/codemasterkapil/smart_attendance_system/blob/main/backend/detection_engine.py)
- Replicate the below hilighted code in line number 10 and 11, and the location of your image accordingly.
- Then add your created variable to the **`known_face_encodings`** List.
- Then add your actual name to the **`known_face_names`** List.
- Then run the application and enjoy the process.

![Code to be changed](https://user-images.githubusercontent.com/81853910/234710539-80e33dc3-8277-48a1-97a0-6b36da1faaa5.png)

## For docker commands

- `docker run <image-name>` - Runs a Docker container from a specified image. 
     
- `docker images` - Lists all the Docker images that are available on your system.    
- `docker ps` - Shows all the running containers on your system.  
- `docker stop` <container-name> - Stops a running Docker container.   
- `docker rm` <container-name> - Removes a stopped Docker container.   
- `docker rmi` <image-name> - Removes a Docker image from your system.   
- `docker pull` <image-name> - Pulls a Docker image from a remote repository.   
- `docker login` - Logs in to a Docker registry so you can push and pull Docker images.
