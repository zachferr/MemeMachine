import sys
import json
import requests
import random
#get synynoms for the words in the sentence that are longer than three characters
def getVerbose(sentence):
    phrase = sentence
    yield phrase
    for i in range(3):
        phrase=getSyns(phrase,i+1)
        yield phrase
def getUrban(sentence,iteration):
    #Given a sentence, change things in the UD most popular list to their UD defs
    words = sentence.split()
    for i in range(len(words)):
        if words[i] in open('list.txt').read():
            phrase = words[i]
            if len(phrase)>6-iteration:
                it=1
                while phrase in open('list.txt').read():
                    if i+it<len(words) and (phrase + words[i+it] in open('list.txt').read()):
                        phrase +=' ' + words[i+it]
                        it+=1
                    else:
                        break
                if len(phrase.split()) > 0:
                    phrase.replace(' ','+')
                    response=requests.get("http://api.urbandictionary.com/v0/define?term="+phrase)
                    UD = response.json()
                    x = UD["list"][0]["definition"]
                    try:
                        return x.split('\r', 1)[0]
                    except:
                        try:
                            return x.split('\n',1)[0]
                        except:
                            return x

def getSyns(sentence, iteration):
    end = ''
    with open("adjAdvMod.json") as data_file:
        data = json.load(data_file)
    for word in sentence.split():
        response = requests.get("http://words.bighugelabs.com/api/2/9a9636f5440c4799c19d84f0fd806c8d/"+word+"/json")
        if len(word) < 6 - iteration :
            end+=word+' '
        else:
            #lots of try shit to see if the word is a verb or a noun
            try:
                syns = response.json()
                #limit is to keep the nyms from getting too weird
                upperlimit=5*iteration

                try:
                    if len(syns["noun"]["syn"])>len(syns["verb"]["syn"]):
                        if len(syns["noun"]['syn']) < upperlimit:
                            upperlimit = len(syns["noun"]['syn'])
                        end+=(random.choice(data["adj"]))+ ' ' + (random.choice(syns["noun"]['syn'][:upperlimit]))+' '
                    else:
                        if len(syns["verb"]['syn']) < upperlimit:
                            upperlimit = len(syns["verb"]['syn'])
                        end+=(random.choice(data["adv"]))+ ' ' + (random.choice(syns["verb"]['syn'][:upperlimit]))+' '
                         
                except:
                    try:
                        if len(syns["noun"]['syn']) < upperlimit:
                            upperlimit = len(syns["noun"]['syn'])
                        end+=(random.choice(data["adj"])) + ' '+ (random.choice(syns["noun"]['syn'][:upperlimit]))+' '
                    except:
                        try:
                            if len(syns["adjective"]['syn']) < upperlimit:
                                upperlimit = len(syns["adjective"]['syn'])
                            end+=(random.choice(syns["adjective"]['syn']))+' '
                        except:
                            try:
                                if len(syns["adverb"]['syn']) < upperlimit:
                                    upperlimit = len(syns["adverb"]['syn'])
                                end+=(random.choice(syns["adverb"]['syn']))+' '
                            except:
                                if len(syns["verb"]['syn']) < upperlimit:
                                    upperlimit = len(syns["verb"]['syn'])
                                end+=(random.choice(data["adv"])) +' '+ (random.choice(syns["verb"]['syn'][:upperlimit]))+' '
            except:
                end+=word+' '
    #end = getUrban(end,iteration)
    return end

if __name__ == "__main__":
    #print(getUrban("a shiny vagoo"))
    words = getVerbose(sys.argv[1])
    for i in range(4):
        print(next(words))