from iso639 import Lang

def get_language_name(code):
    try:
        language = Lang(code)
        return language.name
    except:
        return code
    
def adultNot(code):
    if code==0:
        return "Not"
    else:
        return "Adult"
    
def get_language_code(lan):
    allLan = ['en', 'sv', 'tr', 'es', 'sr', 'cs', 'fr', 'sk', 'ca', 'qbn', 'nl', 'bg', 'ja', 'pt', 'ru', 'qbp', 'uk', 'cmn', 'fa', 'th', 'ka', 'yi', 'de', 'sl', 'hr', 'it', 'hi', 'da', 'gsw', 'he', 'az', 'pl', 'mr', 'gl', 'lt', 'yue', 'ga', 'ar', 'la', 'hy', 'bn', 'te', 'qbo', 'ml', 'bs', 'mk', 'ms', 'id', 'cy', 'qal', 'tl', 'ro', 'uz', 'af', 'et', 'lv', 'ta', 'eu', 'ur', 'eka', 'mi', 'pa', 'gd', 'fi', 'wo', 'tk', 'gu', 'kk', 'tg', 'kn', 'xh', 'ps', 'ku', 'roa', 'ko', 'hu', 'no', 'zu', 'tn', 'st']
    languageList =[]

    lanDic = {}
    for i in allLan:
        languageList.append(get_language_name(i))
        lanDic[get_language_name(i)] = i

    # print(lanDic)
    # print("\n")
    # languageList = set(languageList)
    # print(languageList)
    # print("\n")
    # languageList = list(languageList)
    # print(lanDic[languageList[1]])
    # print(languageList)
    return lanDic[lan]