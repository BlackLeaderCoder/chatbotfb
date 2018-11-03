from fbchat import  Client, log
from fbchat.models import *

class con(Client):
    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        toggle = client.fetchThreadMessages(thread_id=client.uid, limit=1) # client.uid means its our own acc
        for message in toggle:
            pText=message.text.lower()
        if("online" in pText):
            self.markAsRead(author_id)
        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))
        msgText = message_object.text.lower()
        if(msgText=="hi" or msgText=="hii" or msgText=="hiii" or msgText=="slt" or msgText=="salut" or msgText=="salem" or msgText=="slm"):
            reply = "Hello :)"
        elif(msgText=="cv?" or msgText=="cv ?" or msgText=="b1?" or msgText=="bien?" or msgText=="ki rak" or msgText=="صفا" or msgText=="b1?" or msgText=="bien?" or msgText=="ki rak?"):
            reply = "bien hmd et v? :)"
        elif(msgText=="hmd" or msgText=="hmdlh" or msgText=="b1" or msgText=="bien hmd" or msgText=="bien" or msgText=="cv" or msgText=="cv hmd"):
            reply = "hmd ;)"
        elif(msgText=="whatsup" or msgText=="wassup" or msgText=="what's up" or msgText=="wtsup" or msgText=="watsup" or msgText=="whats up" or "how are you" in msgText or "hw r u" in msgText):
            reply = "Awesome. What about you? :)"
        elif(msgText == "kach nv" or msgText == "kachma jdid" or msgText == "heh wach tahki" or msgText == "wach tahki" or msgText == "heh cha tahki" or msgText == "kachma" or msgText == "what's news"):
            reply = "men3andek :)"
        elif (msgText=="heh"):
            reply = "heh :)"
        elif("bye" in msgText or msgText=="byye" or msgText=="byee" or msgText=="by" or msgText=="bn8"):
            reply = "Ok bye! ;)"
        else:
            reply = "manich 7el fb thork robot ta3i howa ali rah yripendi khali message ki n7el nchofo"
        def sendMsgg():
            if (author_id!=self.uid):
                self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
            self.markAsDelivered(author_id, thread_id)
        sendMsgg()
user = input("[*] Enter username :")
passw = input("[*] Enter password :")
client = con(user, passw)
client.listen()
