from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

qasqlite = create_engine(r'sqlite:///dbSQLite.db')

app = Flask(__name__)
api = Api(app)


class MEMBER_TOTAL_WIN_AMOUNT(Resource):
    def get(self):

        MEMBER_ID = request.args.get('MEMBER_ID',None,type=int)
        ACTIVITY_YEAR_MONTH = request.args.get('ACTIVITY_YEAR_MONTH',None,type=int)
        GAME_ID = request.args.get('GAME_ID',None,type=int)

        conn = qasqlite.connect()

        query = ("SELECT MEMBER_ID,sum(WIN_AMOUNT) AS TOTAL_WIN_AMOUNT FROM REVENUE_ANALYSIS WHERE MEMBER_ID=%s"%(MEMBER_ID))

        if ACTIVITY_YEAR_MONTH != None:
            query = query + " AND ACTIVITY_YEAR_MONTH=%s"%ACTIVITY_YEAR_MONTH

        if GAME_ID != None:
            query = query + " AND GAME_ID=%s"%GAME_ID


        query = conn.execute(query)
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'DATA': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient


class MEMBER_TOTAL_WAGER_AMOUNT(Resource):
    def get(self):

        MEMBER_ID = request.args.get('MEMBER_ID',None,type=int)
        ACTIVITY_YEAR_MONTH = request.args.get('ACTIVITY_YEAR_MONTH',None,type=int)
        GAME_ID = request.args.get('GAME_ID',None,type=int)

        conn = qasqlite.connect()

        query = ("SELECT MEMBER_ID,sum(WAGER_AMOUNT) AS TOTAL_WAGER_AMOUNT FROM REVENUE_ANALYSIS WHERE MEMBER_ID='%s'"%MEMBER_ID)

        if ACTIVITY_YEAR_MONTH != None:
            query = query + " AND ACTIVITY_YEAR_MONTH=%s"%ACTIVITY_YEAR_MONTH

        if GAME_ID != None:
            query = query + " AND GAME_ID=%s"%GAME_ID


        query = conn.execute(query)
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'DATA': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient


class MEMBER_TOTAL_WAGERS(Resource):
    def get(self):

        MEMBER_ID = request.args.get('MEMBER_ID',None,type=int)
        ACTIVITY_YEAR_MONTH = request.args.get('ACTIVITY_YEAR_MONTH',None,type=int)
        GAME_ID = request.args.get('GAME_ID',None,type=int)

        conn = qasqlite.connect()

        query = ("SELECT MEMBER_ID,count(*) AS TOTAL_WAGERS FROM REVENUE_ANALYSIS WHERE MEMBER_ID='%s'"%MEMBER_ID)

        if ACTIVITY_YEAR_MONTH != None:
            query = query + " AND ACTIVITY_YEAR_MONTH=%s"%ACTIVITY_YEAR_MONTH

        if GAME_ID != None:
            query = query + " AND GAME_ID=%s"%GAME_ID


        query = conn.execute(query)
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'DATA': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient




api.add_resource(MEMBER_TOTAL_WIN_AMOUNT, '/MEMBER_TOTAL_WIN_AMOUNT/')
api.add_resource(MEMBER_TOTAL_WAGER_AMOUNT, '/MEMBER_TOTAL_WAGER_AMOUNT/')
api.add_resource(MEMBER_TOTAL_WAGERS, '/MEMBER_TOTAL_WAGERS/')


if __name__ == '__main__':
     app.run()
