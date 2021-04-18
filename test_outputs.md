# Here are the some Outputs:

## Test 1
Request :

```
GET: http://127.0.0.1:8000/api/https://storage.googleapis.com/bizupimg/profile_photo/IMG_20200917_190810.jpg
```

Response:
```
{
    "dominant_color": "#fed9e0",
    "logo_border": "#c3a080"
}
```

## Test 2
Request :

```
GET: http://127.0.0.1:8000/api/https://storage.googleapis.com/bizupimg/profile_photo/Screenshot%202020-08-16%20at%205.02.30%20PM%20-%20Nikunj%20Daruka.png
```

Response:
```
{
    "dominant_color": "#eff4f6",
    "logo_border": "#97afc6"
}
```


## Test 3
Request :

```
GET: http://127.0.0.1:8000/api/https://storage.googleapis.com/bizupimg/profile_photo/DigiKarobar-black.jpeg
```

Response:
```
{
    "dominant_color": "#1a1a1a",
    "logo_border": "#917d1c"
}
```

## Test 4
Request :

```
GET: http://127.0.0.1:8000/api/https://storage.googleapis.com/bizupimg/profile_photo/WhatsApp%20Image%202020-08-23%20at%203.11.46%20PM%20-%20Himanshu%20Kohli.jpeg

```

Response:
```
{
    "dominant_color": "#98fd03",
    "logo_border": "#517d26"
}
```