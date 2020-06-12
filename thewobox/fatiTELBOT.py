import telepot
import time
import urllib3

# https://www.pythonanywhere.com/user/wildonion/files/home/wildonion/bot.py?edit
# https://github.com/nickoala/telepot/tree/master/examples/webhook
# https://blog.pythonanywhere.com/148/
# http://telepot.readthedocs.io/en/latest/reference.html#telepot.Bot.getChatAdministrators
# TODO: webhook(flask/aio) - use new bot - start and stop button

# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts
bot = telepot.Bot('495923116:AAF95PqJ_KbN0YJC_iYQTVvbpchWNsICs1I')


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    # print(content_type, chat_type, chat_id)

    if content_type == 'sticker' or 'text' or 'document' or 'photo' or 'audio':
        # admins = [memb['status'] for memb in bot.getChatAdministrators(chat_id)]
        # bot.downloadFile(msg[content_type]['file_id'], msg[content_type]['file_name'])
        # bot.sendMessage(chat_id, "DELETED MESSAGE INFO '{}'".format(msg))
        bot.deleteMessage((chat_id, msg['message_id']))
        # print(msg['message_id'])
    else:
        # admins = [memb['status'] for memb in bot.getChatAdministrators(chat_id)]
        # bot.downloadFile(msg[content_type]['file_id'], msg[content_type]['file_name'])
        # bot.sendMessage(chat_id, "DELETED MESSAGE INFO '{}'".format(msg))
        bot.deleteMessage((chat_id, msg['message_id']))
        # print(msg['message_id'])

def main():
    try:
        bot.message_loop(handle)
        print(bot.getMe())
    except Exception as err:
        print(err)

    while True: # run it forever!
        time.sleep(10)


if __name__ == '__main__':
    main()








