# -*- coding:utf-8 -*-

'''
    收取邮件其实就是创建一个MUA客户端
    从MDA上把邮件内容下载下来 poplib
    把下载下来的文件进行解析 email
'''
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def getMsg():
    #输入邮件地址,授权码,合对应的pop3服务器地址

    email = input('Email:')
    password = input('Password:')
    pop3_srv = 'pop.qq.com'

    # 连接POP3服务器
    srv = poplib.POP3_SSL(pop3_srv)

    # 调试监控
    srv.set_debuglevel(1)
    print(srv.getwelcome().decode('utf-8'))

    # s身份确认
    srv.user(email)
    srv.pass_(password)

    # stat()返回邮件数量合占用空间
    print('Message: %s, Size: %s' % srv.stat())

    # list()返回所有邮件的概述
    resp, mails, octets = srv.list()

    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    print(mails)

    # 获取最新的一封邮件
    index = len(mails)
    resp, lines, octets = srv.retr(index)

    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')

    # 解析邮件
    msg = Parser().parsestr(msg_content)

    srv.quit()

    return msg

# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

# 邮件的Subject或者Email中包含的名字都是经过编码后的str 需要使用decode解码
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
# decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素。上面的代码我们偷了个懒，只取了第一个元素。
# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

if __name__ == '__main__':
    msg = getMsg()
    print(msg)
    print_info(msg,0)