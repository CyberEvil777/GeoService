**Back-end**

![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
![Django](https://img.shields.io/badge/-Django-0aad48?style=flat-square&logo=Django)
![Django Rest Framework](https://img.shields.io/badge/DRF-red?style=flat-square&logo=Django)

**Databases**

![Postgresql](https://img.shields.io/badge/-Postgresql-%232c3e50?style=flat-square&logo=Postgresql)

# GeoService

## Backend
### Чтобы поднять в docker-compose
```powershell
/deploy$ sudo docker-compose up --build
```
### Чтобы поднять ручками в консоли 

Чтобы запустить проект настройте PostGis

```powershell
sudo apt install postgis postgresql-11-postgis-3

psql -h 127.0.0.1 -p 5432 -U YOUR_USER -d YOUR_BD -l

CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
```
Затем накатываем данные с csv файла в бд
```powershell
/src$ python manage.py parse_csv

```
### Проверка запросов

запрос выглядит следующим образом

http://127.0.0.1:8000/api/geolocation/?address=хабаровск+дикапольцева+12&diametr=1000

