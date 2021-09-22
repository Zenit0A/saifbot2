








messagee='spam py saif'
from googletrans import Translator
import os
whiteList=['a222da24-92d5-490b-a2c0-1acb609902b8']
from time import sleep as sl
from threading import Thread as th
import samino
c=samino.Client('220B50483BB71470AE607E8A0AD2834BC286F0E1AF76CF1FEAEB74BBA38CF28ED18D58EB6A0E867FF6')
em='coxab48957@dmsdmg.com'
pa='amonguslivewallpape88'
lol=c.get_from_link('http://aminoapps.com/p/uquks8')
c.login(em,pa)
chatt=lol.objectId
blackList=['2932c23c-2d78-47a2-8fe3-1c93aa887064']
local=samino.Local(lol.comId)
local.send_message(chatt,'._.')
@c.event("on_message")
def on_message(data: samino.lib.Event):
	content=data.message.content
	comId=data.ndcId
	msgId=data.message.messageId
	chatId=data.message.chatId
	msg=data.message.content
	if msg.startswith("!tr"):
		text = Translator().translate(text=data.message.replyMessage.content, dest=msg.split(" ")[1]).text
		local.send_message(chatId, f"""{text}""", replyTo=msgId)
		pass
	if msg.startswith('!prov'):
		uoper=data.message.userId
		lollll=c.get_user_info(uoper)
		niikk=lollll.nicknamd
		messop=f'hi {niikk}'
		local.start_chat(uoper,messop)
		local.send_message(chatId,'تم الدخول لخاصك',replyTo=msgId)
	if msg.startswith('!start.vc'):
		user=data.message.userId
		if user in whiteList:
			local.start_vc(chatId)
			local.send_message(chatId,'تم بدا الدردشه الصوتيه',replyTo=msgId)
		else:
			local.send_message(chatId,'عذرا انت لست من القائمه البيضاء',replyTo=msgId)
	if msg.startswith('!end.vc'):
		user=data.message.userId
		if user in whiteList:
			local.end_vc(chatId)
			local.send_message(chatId,'تم انهاء الدردشه الصوتيه',replyTo=msgId)
		else:
			local.send_message(chatId,'عذرًا انت لست من القائمه البيضاء',replyTo=msgId)
	if msg.startswith('!id'):
		if 'http' in msg:
			comId=c.get_from_link(msg[4:]).comId
			chatId=c.get_from_link(msg[4:]).objectId
			local.send_message(chatId,f'comId :{comId}\nchatId: {chatId}',replyTo=msgId)
	if msg.startswith('!kick'):
		userr=data.message.userId
		if userr in whileList:
			uosr=c.get_from_link(msg[6:]).objectId
			local.kick(chatId,uosr)
			local.send_message(chatId,'تم طرد العضو بنجاح',replyTo=msgId)
		else:
			local.send_message(chatId,'عفوا انت لست من القائمه البيضاء',replyTo=msgId)
	if msg.startswith('!follow'):
		if 'http' in msg:
			sopq=c.get_from_link(msg[8:]).objectId
			local.follow(sopq)
			local.send_message(chatId,'تم متابعة العضو',replyTo=msgId)
	if msg.startswith('!unview'):
		userl=data.message.userId
		if userl in whiteList:
			local.chat_settings(chatId,viewOnly=False)
			local.send_message(chatId,'تم اغلاق وضع الاطلاع',replyTo=msgId)
		else:
			local.send_message(chatId,'عذرا انت لست من القائمه البيضاء',replyTo=msgId)
	if msg.startswith('!follow.me'):
		usqy=data.message.userId
		local.follow(usqy)
		local.send_message(chatId,'تم متابعتك',replyTo=msgId)
	if msg.startswith('!daily'):
		local.send_message(chatId,'بدأ ارسال القروش',replyTo=msgId)
		useerri=data.message.userId
		for _ in range(200):
			th(target=c.watch_ad,args=(useerri, )).start()
	if msg.startswith("!view"):
		userId=data.message.userId
		if userId in whiteList:
			local.chat_settings(chatId,viewOnly="enable")
			local.send_message(chatId,'تم فتح وضع الاطلاع فقط',replyTo=msgId)
		else:
			local.send_message(chatId,"عذرا انت لست من القائمة البيضاء",replyTo=msgId)
	if msg.startswith('!join'):
		if 'http' in msg:
			opqo=c.get_from_link(msg[6:]).objectId
			local.join_chat(opqo)
			local.send_message(chatId,'تم الدخول للشات',replyTo=msgId)
	if content.startswith('!msg'):
		mess=content[5:]
		local.send_message(chatId,mess,replyTo=msgId)
	if msg.startswith("!info"):
				if 'http' in msg:
					usrl=c.get_from_link(msg[6:]).objectId
					dono=c.get_user_info(usrl)
					name2=dono.nickname
					icon2=dono.icon
					create=dono.createdTime
					ser=dono.content
					ID=data.message.userId
					local.send_message(chatId,
			'[c]-nickname: '+name2+'''
[c]-'''
'''icon: '''+icon2+'''
[c]-'''
'''id: '''+ID+'''
[c]-'''
f'''the time create for account: {create}'''+'''
[c]-'''
f''' content: {ser}'''
,replyTo=msgId)
	if msg.startswith('!help'):
		local.send_message(chatId,'''
[c] ملاحظه:
[c] بادئة الاوامر !
[c]!daily لارسال القروش لك
[c]!info [رابط الشخص] لارسال معلومات الشخص
[c]!msg [الرساله] لارسال الكلمة التي بعد الامر
[c]!follow.me لمتابعتك
[c]!follow [رابط الشخص] لمتابعة العضو الذي تم ارسال رابطه
[c]!id [رابط القروب] لاستخراج ايدي القروب وايدي المنتدى
[c]!tr لترجمة النص الذي ترد عليه 
[c] ملاحظة لامر الترجمه:
[c] لترجمة النص يجب الرد على الرساله ب امر!tr وكتابة اول حرفين من اللغة الذي تريد ترجمت النص اليها
[c] اوامر الوايت ليست:
[c]!unview لالغاء وضع الاطلاع
[c]!view لفتح وضع الاطلاع
[c]!start.vc لبدء دردشه صوتيه
[c]!end.vc لانهاء الدردشه الصوتيه
''',replyTo=msgId)

@c.event("on_member_join")

def on_join(data: samino.Event):

    local = samino.Local(data.ndcId)

    user=data.message.userId
    chatId = data.message.chatId

    nickname = data.message.author.nickname

    local.send_message(chatId, "welcome to the chat",embedLink="ndc://user-profile/"+user,embedTitle=nickname)
@c.event('on_member_left')
def on_member_left(data):
	user=data.message.userId
	m3lm=c.get_user_info(user)
	nickname=m3lm.nickname
	local.send_message(chatId,'bye bye '+nickname)
print('تم')
c.launch()