import random
import json
from enums.category import Category


def getFileName(category):
    fileName = 'questions/questions.json'
    return fileName


def getCategoryQuestions(data, category):
    result = ''
    for x in data:
        if(x['category'] == Category(category).name):
            result = x['questions']
            break
    return result


def getRandomQuestion(category=Category.Discuss.value):
    try:
        fileName = getFileName(category)
        with open(fileName, 'r') as f:
            data = json.load(f)
            id = random.randint(0, len(data)-1)
            data = getCategoryQuestions(data,category)
            text = data[id]
            return text
    except Exception as e:
        print(e)


def getRandomQuestionWithId(id, category=Category.Discuss.value):
    try:
        fileName = getFileName(category)
        with open(fileName, 'r') as f:
            data = json.load(f)
            data = getCategoryQuestions(data,category)
            text = data[id]
            return text
    except Exception as e:
        print(e)


def getQuestionsLen(category=Category.Discuss.value):
    result = None
    try:
        fileName = getFileName(category)
        with open(fileName, 'r') as f:
            data = json.load(f)
            data = getCategoryQuestions(data,category)
            result = len(data)
    except Exception as e:
        print(e)
    return result


