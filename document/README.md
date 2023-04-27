# httpie 

```
http --form http://10.25.10.132:8006/api/user/login username=limr1209 password=admin123
http http://10.25.10.132:8006/admin/face_image/list 'Cookie:session=9be8095e-1f9f-4cf3-ae31-8e5aab4584f7.5u60CrWZlyR-KacjSLA-vy9xSoo'
http --form post http://10.25.10.132:8006/admin/face_image_auto/save file@facemodel/face_image/00018-1485885527.png 'Cookie:session=9be8095e-1f9f-4cf3-ae31-8e5aab4584f7.5u60CrWZlyR-KacjSLA-vy9xSoo' name=哈哈
```


# git

# linux 

```
scp -r .\ExportClient\ mei@10.25.20.15:/opt/projects/facemodelapidev/u3dbuild/
ssh mei@10.25.20.15: "chmod +x /opt/projects/facemodelapidev/u3dbuild/ExportClient/Client.x86_64"
```
