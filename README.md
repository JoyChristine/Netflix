# Netflix
A netflix clone created entirely using Django.
![image](https://user-images.githubusercontent.com/57414671/171838640-e9618d0a-a2dd-404f-a68e-ea54fd50470c.png)



## Description
User can sign up and login
After login user is able to view the various movie shows
### Prerequisites

# Setup and Installation  

  
#### Cloning the repository:  
 ```bash 
https://github.com/JoyChristine/Netflix.git
```
#### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations art
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py runserver 
```
The application opens up on `127.0.0.1:8000`. <br>
If you want to use new server run e.g 9000
```bash 
 python manage.py runserver 9000
```
##### Testing the application  
 ```bash 
 python manage.py test art
```
# TO-DO
1. Display various categories of movies using the API
2. Show various users signed in
3. Improve UI
4. Implement youtube API to play trailers
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 4.0.4](https://docs.djangoproject.com/en/4.0/)  
* [Heroku](https://heroku.com)  
  


## Authors

* **[Joy Christine](https://github.com/JoyChristine)** 



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


