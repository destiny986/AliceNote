# AliceNote
**Аддон для RTools - отправка голосовых оповещений Яндекс Алисе с помощью клиент-api TG.**  

Конфигурация в .env по адресу  
```
%LOCALAPPDATA%/RTools/.env
```
В формате
```
CLIENT_NAME = 'name'     # название файла для кэша авторизации
ACC_ID = 123456789       # api_id аккаунта от которого идет запрос Алисе
ACC_HASH = 'hash'        # api_hash аккаунта от которого идет запрос Алисе
```
Фразы по адресу 
```
%LOCALAPPDATA%/RTools/AlicePhrases.txt
```
Формат сообщений боту по типу
```
/s Hello world
/s Hello world again
```
