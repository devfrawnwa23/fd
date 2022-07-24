import asyncio
from pyrogram import Client
import re
api_id = 8468696
api_hash = "23757c1adfb53a73fbea5df91fac5a9e"
token = input("Enter Token : ")
bot_id = re.findall('[0-9]+', token)[0]
id = input("Enter group id or username : ")
app = Client("bott", bot_token=token, api_id = api_id, api_hash = api_hash)

@app.on_message()
async def num(client, message):
    i = 1
    xx = 1
    async for x in app.get_chat_members(id):
      if int(x.user.id) != bot_id :
        try :
          await app.ban_chat_member(id,x.user.id)
          print(f"• done {i}")
          i += 1
        except Exception as e:
          print(f"• fail {xx}        {e}")
          xx +=1
        
    print(f"• تم حظر {i} عضو \n• لم استطيع حظر {xx} عضو")


app.run()