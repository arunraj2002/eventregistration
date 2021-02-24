# WebApplication for Event Registration

## AIM:
To create a UX design and develop a web application for event registration.
## DESIGN STEPS:
![output](./static/img/desin.png)


## DESIGN SCREENS:
![output](./static/img/homep.png)

![output](./static/img/regp.png)

![output](./static/img/tabp.png)

![output](./static/img/sp.png)

![output](./static/img/fp.png)


## WIREFRAME:
![output](./static/img/wire.png)



## PROTOTYPE:
![output](./static/img/proto.png)

![output](./static/img/homep.png)


![output](./static/img/regp.png)

![output](./static/img/tabp.png)

![output](./static/img/sp.png)

![output](./static/img/fp.png)



## PROGRAM:

### home.html:
```
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>SAVEETHA ENGINEERING COLLEGE</title>
    <style>
        .img{
            background-size: cover;
            height: 550px;
            width: 1550px;
            background-image: url('https://png.pngtree.com/thumb_back/fw800/background/20190223/ourmid/pngtree-smart-robot-arm-advertising-background-backgroundrobotblue-backgrounddark-backgroundlightlight-image_68405.jpg');
        }
    </style>
</head>

<body>
    <div class="jumbotron">
        <div class="text-center">
            <h1 class="display-8">Robotics Event</h1>
            <div>Learn to master the skills on robotics
            </div>
        </div>
    </div>
    <div class="p-5 text-center bg-image img" >
        <div class="text-right">
            <div class="text-white">
                <h1 class="mb-3">PLACE: SAVEETHA ENGINEERING COLLEGE</h1>
                <h4 class="mb-3">Join Our Free Online Workshop,</h4>
                <h4 class="mb-3">On 27/02/21 at 3pm</h4>
                <a href="/register/" class="btn btn-outline-light btn-lg" role="button">Register Now</a>
            </div>
        </div>
    </div>
    <!-- Background image -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous">
        </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous">
        </script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous">
        </script>
</body>

</html>
```

### register.html:
```
    <!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Registration Form</title>
</head>

<body>
    <div class="jumbotron jumbotron-fluid">
        <div class="container text-center">
            <h1 class="display-8">CyberSecurity</h1>
            <div>Privacy has been a greater issue in the modern world and in this event we will teach you how to protect your privacy.
            </div>
        </div>
    </div>
    <div class="container ">
        <div class="col-12 ">
            <form action="" method="POST">
                {% csrf_token %}
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" class="form-control" id="username" placeholder="Enter your Name" name="username" required>
                </div>
                <div class="form-group">
                    <label for="institute">Name of Your College/University</label>
                    <input type="text" class="form-control" id="institute" name="institute" placeholder="Enter the Name of the Institute" required>
                </div>

                <div class="form-group">
                    <label for="emailid">Email Address</label>
                    <input type="email" class="form-control" id="emailid" name="emailid" placeholder="Enter email" required>
                    <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                </div>
                <div class="form-group">
                    <label for="number">Phone</label>
                    <input type="text" class="form-control" id="phnumber" name="phnumber" placeholder="Contact Number" required>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
                <a href="/invite/" class="btn btn-primary" role="button">Cancel</a>
            </form>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>
</html>
```

### listofparticipants.html:
```
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>List of Participants</title>
</head>

<body>
    <div class="jumbotron jumbotron-fluid">
        <div class="container text-center">
            <h1 class="display-8">RoboFest</h1>
        </div>
    </div>
    <div class="container">
        <h1>LIST OF PARTICIPANTS</h1>
        <table class="table  table-striped table-dark">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Contact number</th>
                    <th scope="col">Institute</th>

                </tr>
            </thead>
            <tbody>
                {% for col in participant %}

                <tr >
                    <td> {{col.name}}</td>
                    <td>{{col.inst}}</td>
                    <td>{{col.email}}</td>
                    <td>{{col.contnum}}</td>

                </tr>
                {% endfor %}


            </tbody>
        </table>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>

</html>
```

### success.html:

```
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Saveetha Engineering College</title>
</head>

<body>
    <div class="jumbotron">
        <div class="container">
            <h1 class="display-4">Robotics Event</h1>
            <p class="lead">An Interaction with Robotics</p>
            <hr class="my-4">
            <p>The participants will be exposed to problem-solving activities, infrastructure of Robotics and future of
                Robotics.</p>
            <p class="lead">

            </p>
        </div>
    </div>

    <div class="container">
        <div class="row">
            <div class="col-12">

                <h1>Congragulations!You're in.</h1>
                <p class="lead">We hope you have fun and learn more about robotics. Thank You and Have a great day.

                </p>
            <a href="/home/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">Home</a>
    </div>

                <!-- Optional JavaScript -->
                <!-- jQuery first, then Popper.js, then Bootstrap JS -->
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
                    integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
                    crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
                    integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
                    crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
                    integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
                    crossorigin="anonymous"></script>
</body>

</html>
```


### failed.html:
```

<!doctype html>
<html lang="en">
 
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Failed</title>
</head>

<body>
    <div class="jumbotron jumbotron-fluid">
        <div class="container text-center">
            <h1 class="display-8">RoboFest</h1>
        </div>
    </div>
    <div class="container text-center ">
        <h1 >Oops! Better Luck Next Time, No More Registration Available</h1>
    </div>

    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>

</html>
```


### views.py:
```
from django.shortcuts import render
from .models import Participant, ParticipantAdmin
# Create your views here.
def home(request):
    context={}
    return render(request,"eventapp/home.html",context)

def register(request):
    context={}
    if request.method == 'POST':
        p1 = Participant()
        p1.name = request.POST.get('username','-')
        p1.inst = request.POST.get('institute','-')
        p1.email = request.POST.get('emailid','-')
        p1.contnum = request.POST.get('phnumber','000')

        if len(Participant.objects.all()) > 10:
            return render(request, 'eventapp/failure.html',context)
        else:
            p1.save()
            return render(request, 'eventapp/success.html',context)

    if request.method == 'GET':
        context['name'] = ''
        context['inst'] = ''
        context['email'] = ''
        context['contnum'] = ''

    return render(request,"eventapp/register.html",context)
    
def listofparticipants(request):
    context={}
    context['participants'] = Participant.objects.all()
    return render(request,"eventapp/participants.html",context)


def success(request):
    context={}
    return render(request,"eventapp/success.html",context)

def fail(request):
    context={}
    return render(request,"eventapp/failure.html",context)
```

### models.py:
```
from django.db import models
from django.contrib import admin
# Create your models here.

class Participant(models.Model):
    name=models.CharField(max_length=20)
    inst=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    contnum=models.CharField(max_length=15)

class ParticipantAdmin(admin.ModelAdmin):
    list_display=("name","inst","email","contnum")
```

## OUTPUT:


![output](./static/img/homeo.png)

![output](./static/img/ro.png)

![output](./static/img/po.png)

![output](./static/img/suco.png)

![output](./static/img/filo.png)


## RESULT:
        Thus, a UX design and develop a web application for event registration has been done for http://arun.student.saveetha.in:8000/home/ .