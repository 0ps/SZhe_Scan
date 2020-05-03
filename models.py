from exts import db
from datetime import datetime

'''
存放模型
'''
class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    email=db.Column(db.String(20),nullable=False)
    username=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(100),nullable=False)

#boolcheck  ->true 即 ip       ->false 即 domain
class BaseInfo(db.Model):
    __tablename__='baseinfo'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    boolcheck=db.Column(db.Boolean,nullable=True)
    url=db.Column(db.String(50),nullable=False)
    status=db.Column(db.String(3),nullable=False)
    title=db.Column(db.String(50),nullable=True)
    date=db.Column(db.String(30),nullable=False)
    responseheader=db.Column(db.Text,nullable=False)
    Server = db.Column(db.String(100),nullable=True)
    portserver = db.Column(db.Text,nullable=True)
    senmessage = db.Column(db.Text,nullable=True)
    sendir = db.Column(db.Text,nullable=True)


class IPInfo(db.Model):
    __tablename__='ipinfo'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    baseinfoid=db.Column(db.Integer,nullable=False)
    bindingdomain=db.Column(db.Text,nullable=True)
    sitestation=db.Column(db.Text,nullable=True)
    CMessage=db.Column(db.Text,nullable=False)
    ipaddr=db.Column(db.String(100),nullable=False)

class DomainInfo(db.Model):
    __tablename__='domaininfo'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    baseinfoid=db.Column(db.Integer,nullable=False)
    subdomain=db.Column(db.Text,nullable=True)
    whois=db.Column(db.Text,nullable=True)
    bindingip=db.Column(db.Text,nullable=True)
    sitestation=db.Column(db.Text,nullable=True)
    recordinfo=db.Column(db.String(100),nullable=True)
    domainaddr=db.Column(db.String(100),nullable=True)

class BugList(db.Model):
    __tablename__='buglist'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    oldurl=db.Column(db.String(50),nullable=True)
    bugurl=db.Column(db.String(50),nullable=True)
    bugtype=db.Column(db.Text,nullable=True)
    buggrade=db.Column(db.String(10),nullable=True)
    bugdetail=db.Column(db.Text,nullable=True)

class SeriousBug(db.Model):
    __tablename__='seriousbug'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class HighBug(db.Model):
    __tablename__='highbug'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class MediumBug(db.Model):
    __tablename__='mediumbug'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class LowBug(db.Model):
    __tablename__='lowbug'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Log(db.Model):
    __tablename__='log'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip=db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    date=db.Column(db.DateTime,default=datetime.now)