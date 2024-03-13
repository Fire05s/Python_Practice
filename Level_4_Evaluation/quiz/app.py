from flask import *
import pymongo
from passlib.hash import pbkdf2_sha256

client = pymongo.MongoClient("mongodb+srv://[USER]:[PASSWORD]@cluster0.ookfz.mongodb.net/?retryWrites=true&w=majority")
db = client.quiz

app = Flask(__name__)

app.secret_key = '279t8sklvsn'
loggedin = False
subject = ''
short = ''
session = {}
quiznum = 0

@app.route ('/',methods = ['GET','POST'])
def home ():
    global loggedin,subject,session
    if request.method == 'GET':
        if session == {}:
            loggedin = False
            return render_template ('home.html',loggedin = loggedin)
        else:
            loggedin = True
            questions = db.questions.find ()
            geo = 0
            math = 0
            sci = 0
            for set in questions:
                if 'geo' in set['subject']:
                    geo += 1
                elif 'math' in set['subject']:
                    math += 1
                elif 'science' in set['subject']:
                    sci += 1
            attgeo = 0
            attmath = 0
            attsci = 0
            for att in session ['att_quiz']:
                if att == 'Geography':
                    attgeo = len (session ['att_quiz'][att])
                elif att == 'Math':
                    attmath = len (session ['att_quiz'][att])
                elif att == 'Science':
                    attsci = len (session ['att_quiz'][att])
            return render_template ('home.html',loggedin = loggedin, geo = geo,math = math,sci = sci,attgeo = attgeo,attmath = attmath,attsci = attsci)
    if request.method == 'POST':
        if 'geo' in request.form:
            subject = 'Geography'
            return redirect ('/quiz')
        if 'math' in request.form:
            subject = 'Math'
            return redirect ('/quiz')
        if 'science' in request.form:
            subject = 'Science'
            return redirect ('/quiz')
        if 'reg' in request.form:
            reguser = request.form ['reguser']
            regpass = request.form ['regpass']
            regpass = pbkdf2_sha256.hash(regpass)
            db.accounts.insert_one ({'user':reguser,'password':regpass,'att_quiz':{}})
            flash ('Your account has been registered.')
            return redirect ('/')
        if 'log' in request.form:
            loguser = request.form ['loguser']
            logpass = request.form ['logpass']
            try:
                account = db.accounts.find_one ({'user':loguser})
                if pbkdf2_sha256.verify(logpass, account['password']):
                    session ['user'] = loguser
                    session ['answers'] = []
                    session ['score'] = 0
                    session ['att_quiz'] = account ['att_quiz']
                    flash ('You have been logged in.')
                    print (session)
                else:
                    flash ('Password is incorrect')
            except:
                flash ('User does not exist.')
            return redirect ('/')
        if 'logout' in request.form:
            session = {}
            return redirect ('/')

@app.route ('/quiz',methods = ['GET','POST'])
def quiz ():
    global session,short,subject,quiznum
    if request.method == 'GET':
        print (session,subject)
        if 'user' in session:
            if short == '':
                if subject == 'Geography':
                    short = 'geo'
                elif subject == 'Math':
                    short = 'math'
                elif subject == 'Science':
                    short = 'science'
            print (short)
            questions = db.questions.find_one ({'subject':short})
            return render_template ('quiz.html',subject = subject,questions = questions,session = session)
        else:
            flash ('Login before trying a quiz.')
            return redirect ('/')
    if request.method == 'POST':
        if 'quizsubmit' in request.form:
            questions = db.questions.find_one ({'subject':short})
            score = 0
            session ['answers'] = []
            for loop in range (0,5,1):
                if request.form[questions['q'][loop]['question']] == questions ['q'][loop]['correct']:
                    score += 1
                session ['answers'].append (request.form [questions['q'][loop]['question']])
            session ['score'] = score
            
            print ('session 1: ',session)
            if subject not in session['att_quiz']:
                session ['att_quiz'][subject] = {}
            print ('session 2: ',session)
            session ['att_quiz'][subject][short] = score
           
            # implement push for subjects not already in att_quiz and set for those already in
            # curruser = db.accounts.find_one ({'user':session['user']})
            # if subject in curruser ['att_quiz']:
            db.accounts.update_one ({'user':session ['user']},{'$set':{'att_quiz':session['att_quiz']}})
            # else:
            #     db.accounts.update_one ({'user':session ['user']},{'$push':{'att_quiz':{subject:session['att_quiz']}}})
            return redirect ('/quiz')
        if 'return' in request.form:
            subject = ''
            short = ''
            quiznum = 0
            session ['answers'] = []
            session ['score'] = 0
            # session ['att_quiz'] = {}
            return redirect ('/')
        if 'nextquiz' in request.form:
            session ['answers'] = []
            session ['score'] = 0
            if quiznum < 1:
                quiznum += 1
                short += str (quiznum)
                questions = db.questions.find_one ({'subject':short})
                return render_template ('quiz.html',subject = subject,questions = questions,session = session)
            else:
                subject = ''
                short = ''
                quiznum = 0
                flash ('You have finished all available quizzes for this subject.')
                return redirect ('/')

app.run (debug = True)