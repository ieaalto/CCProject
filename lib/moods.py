from config import settings


def group_keyword(keyword, model):
    maximum = None
    best = None

    for feature in settings.MOODS:
        score = max([model.similarity(k, keyword) for k in settings.MOODS[feature]])
        if not maximum or score > maximum :
            maximum = score
            best = feature

    return best


