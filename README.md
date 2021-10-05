### Simple discord bot
This bot is simple music bot for discord
- prefix => "d!"
---

#### General commands:
- help - displays all the available commands
---

#### Music commands:
- play (p) <keywords> - finds the song on youtube and plays it in your current channel
- queue (q) - displays the current music queue
- skip (s) - skips the current song being played
- disconnect (dc) - disconnects the bot from voice channel
---
 
#### bot.py
* Responsible for handling all the discord API stuff
---
 
#### Installation
* need to install the following libraries
  * pip install discord.py[voice]
  * pip install youtube_dl
 ```python
  python -m pip install -d requirements.txt
  ```
