client_org.xlsx

Состоит из двух листов client и organization.

В листе client поле name уникально. 

В листе organization список компаний клиента (client_name + name уникально).

bills.xlsx

Это список счетов организации клиента. Уникальность по полям client_org и №.

+Необходимо реализовать загрузку этих файлов через api и заполнить БД (SQLite или PostgreSQL) находящимися записями.
+Условие уникальности записей должно сохраняться и в БД.

+Это должно быть api с использованием Django REST framework:

+1. эндпоинт загрузки файлов bills.xlsx и client_org.xlsx  (может быть по одному на файл, как посчитаете правильным)

Эндпоинт один на любой из двух файлов. По названию файла определяет, что с ним делать.
POST: http://127.0.0.1:8000/api/upload

-2. эндпоинт со списком клиентов
Данные, которые нужно отдавать для каждого элемента списка:
 - Название клиента
 - Кол-во организаций
 - Приход (сумма по счетам всех организаций клиента)

-3. эндпоинт со списком счетов с возможностью фильтровать по организации или по клиенту

Эндпоинты проекта
GET:
http://127.0.0.1:8000/api/client
http://127.0.0.1:8000/api/organization
http://127.0.0.1:8000/api/bill
