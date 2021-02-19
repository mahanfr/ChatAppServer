# ChatAppServer
chat server using django and django-channels

## Install
Make sure to install reddis from https://github.com/tporadowski/redis/releases

### dependencies
* python 3.7.8
* django
* channels
* channels_redis

## Testing and Development
This code is under development and has security issues

### testing
For testing WebSockets you can use <a href="https://github.com/asleepysamurai/socketwrench">Socket Wrench</a></br>
For testing Api you can use <a href="https://www.postman.com/downloads/">Postman</a></br>

For sending a new message to char "room" you can use this json format</br>
MAKE SURE YOU ALREADY MADE A CHAT AND CONTACT INSIDE DATABASE
```json
{
    "command":"new_message",
    "from":"YOUR_NAME",
    "chatId":1,
    "message":"YOUR_MESSAGE"
}
```
For Getting all messages(resent 10) of a room
```json
{
    "command":"fetch_messages",
    "chatId":1
}
```