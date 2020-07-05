import db.db as db
import json
import questions
import sys
from enums.category import Category
import random

sqlExist = '''SELECT count(*) FROM UserSession
                WHERE UserId = ?'''
sqlInsert = '''INSERT INTO  UserSession
                (
                    UserId,
                    ListQuestion
                )
                VALUES
                (   ?, -- UserId - integer
                    ?   -- ListQuestion - nvarchar(max)
                )'''
sqlUpdate = '''
UPDATE UserSession
SET ListQuestion = ?
WHERE UserId = ?
'''
sqlSelectUserData = '''
SELECT ListQuestion FROM UserSession
WHERE UserId = ?
'''


def generateQuestionIdsArray(n):
    arr = []
    for i in range(0, n):
        arr.append(i)
    return arr


def generateObject():
    list = []
    try:
        for item in Category:
            myObject = {'category': item.value,
                        'questionIds': generateQuestionIdsArray(questions.getQuestionsLen(item.value))}
            list.append(myObject)
    except Exception as e:
        print(e)
    return json.dumps(list)


class Session:
    def __init__(self, userId, category):
        self.userId = userId
        self.category = category

    def getQuestionId(self):
        try:
            exist = db.select(sqlExist, [self.userId])
            if(exist[0][0] == 0):
                myObject = generateObject()
                db.execute(sqlInsert, [self.userId, myObject])

            data = db.select(sqlSelectUserData, [self.userId])
            data = json.loads(data[0][0])
            id = None
            for x in data:
                if x['category'] == self.category:
                    if(len(x['questionIds']) == 0):
                        x['questionIds'] = generateQuestionIdsArray(questions.getQuestionsLen(
                            self.category))  # don't need -1 because of range(0,n)
                    id = x['questionIds'].pop(
                        random.randint(0, len(x['questionIds'])-1))

                    myObject = json.dumps(data)
                    db.execute(sqlUpdate, [myObject, self.userId])
                    break
            return id
        except Exception as e:
            print(e)




