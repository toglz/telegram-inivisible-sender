[English readme.md](#english-readme) 
# <a name="russian-readme"></a> Скрипт для отправления невидимых (Для отправителя) сообщений в Telegram

Скрипт, позволяющий отправлять самоуничтожающиеся (Только для отправителя) сообщения пользователям Telegram

## **Установка**
— Распаковать загруженный архив в любую директорию.
— Запустить консоль в директории где был распакован архив и выполнить команду:
```
pip install -r requirements.txt
```

## **Настройка**
### Обязательно укажите следующие данные перед запуском скрипта:

* `api_id` — Api Id вашего Telegram аккаунта
* `api_hash` — Api Hash вашего Telegram аккаунта
> Вы можете получить эти 👆👆👆 значения на сайте [my.telegram.org](my.telegram.org)
* `message` — Это сообщение будет отправляться пользователям из *users_db.txt*
* `users_db.txt` — Файл с именами пользователей в следующем формате:

```
@user1
@user2
@user3
-----или-----
user1
user2
user3
```

### Другие переменные:

* `database_filename` — Название файла с пользователями без расширения
* `what_to_hide` — Что удалять при отправке сообщения
    * `message` - Удалять сообщение *(Для отправителя)*
    * `chat` *(Значение по умолчанию)* - Удалять чат в котором было отправлено сообщение *(Для отправителя)*
    
> Следующие значения 👇👇👇 не рекомендуется менять во избежание блокировки вашего Telegram аккаунта
* `sending_delay` *(30 секунд по умолчанию)* — Задержка до отправки следующего сообщения в секундах
* `max_messages` — Максимально допустимое количество сообщений отправленных за сессию

[Русский readme.md](#russian-readme)
# <a name="english-readme"></a>Telegram invisible messages sender
# A script for sending invisible (sender only) messages to Telegram

A script that allows you to send self-destructing (sender only) messages to Telegram users

## **Installation**
- Extract the downloaded archive to any directory.
- Run the console in the directory where you unpacked the archive and run the command:
```
pip install -r requirements.txt
```

## **Setup**
### Be sure to enter the following data before running the script:

* `api_id` - Api Id of your Telegram account
* `api_hash` - Api Hash of your Telegram account
> You can get these 👆👆👆 values at [my.telegram.org](my.telegram.org)
* `message` - This message will be sent to users from *users_db.txt
* `users_db.txt` - File with user names in the following format:

```
@user1
@user2
@user3
----- or -----
user1
user2
user3
```

### Other variables:

* `database_filename` - Name of the file *(without an extension)* containing user names
* `what_to_hide` - What to delete when sending a message
    * `message` - To delete the message *(For the sender)
    * `chat` *(Default value)* - Delete the chat in which the message was sent *(For the sender)
    
> The following 👇👇👇 values are not recommended to change to avoid blocking your Telegram account
* `sending_delay` *(30 seconds by default)* - Delay before the next message is sent in seconds
* `max_messages` - Maximum number of messages sent per session
