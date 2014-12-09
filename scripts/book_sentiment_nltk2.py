import nltk, re, pprint
from nltk import word_tokenize, FreqDist, pos_tag
import os,ast

def find_fdist(text_name):
    raw = open(text_name,'r', encoding = 'utf8')
    text_name = raw.read()
    tokens = word_tokenize(text_name)
    raw.close()

    noun_list = list()

    pos_tokens = nltk.pos_tag(tokens)
    for token in pos_tokens:
        if(token[1] == "NN" or token[1] == "NNS" or token[1] == "NNP" or token[1] == "NNPS"):
            noun_list.append(token[0])
    fdist1 = FreqDist(noun_list)
    return fdist1

def get_top_nouns_for_all():
    for root,dirs,files in os.walk("C:/Users/Anne/IdeaProjects/BookSelfie/text"):
        for filename in files:
            print("Starting " + filename)
            filename = os.path.join(root, filename)
            fdist = find_fdist(filename)
            with open("top_200_nouns.txt", "a")as f:
                f.write(str(fdist.most_common(200))+',\n')
    print("Done!")

def get_concept_count_for_all(name1, name2, array1, array2):
    aggregate_count = [0,0]
    with open("concept_count.txt","a") as f:
        f.write("[")
    for root,dirs,files in os.walk("C:/Users/Anne/IdeaProjects/BookSelfie/text"):
        for filename in files:
            print("Starting " + filename)
            full_filename = os.path.join(root, filename)
            concept_count = find_concept_count(full_filename, array1,array2)
            with open("concept_count.txt", "a") as f:
                aggregate_count[0] += concept_count[0]
                aggregate_count[1] += concept_count[1]
                f.write("['" +str(filename) + "', '" +
                    str(name1)+ ": " + str(concept_count[0])+"','" + str(name2)+ ": " + str(concept_count[1])+
                        "', 'Percentage of "+name1+": " + str(concept_count[0]/(concept_count[1]+concept_count[0]))+"'],\n")
    with open("concept_count.txt", "a") as f:
        f.write("['Aggregate Count', '" + str(aggregate_count[0]) + "', '"+str(aggregate_count[1])+
                "',"+"'Percentage of "+name1+": " + str(aggregate_count[0]/(aggregate_count[0]+aggregate_count[1]))+"']],\n\n")

def find_concept_count(file, array1, array2):
    count = [0,0]
    with open(file, "r", encoding = 'utf8') as f:
        tokens = word_tokenize(f.read())
        for word in tokens:
            for item in array1:
                if word == item:
                    count[0]+=1
            for item in array2:
                if word == item:
                    count[1]+=1
    return count


'''

get_concept_count_for_all("love", "hate", ['love', 'loving','loved','lover','loves','lovers'],
                          ['hate', 'hating','hated', 'hater','hates','haters'])

get_concept_count_for_all("peace","war",['peace','peaceful','unity','harmony','truce','tranquility'],
['war','battle','wars','battles','fight','fighting','fought','fights'])

get_concept_count_for_all("victory","defeat",['victory','victorious','win','winner','winning','wins','won','triumph','accomplishment'],
['loss','lose','losing','lost','defeated','surrender','beaten','vanquished','destroyed'])

get_concept_count_for_all("happiness","tragedy",['happiness','happy','joy','joyous','bliss',
                                                 'laughter','laugh','pleasure','laughs','enjoy','enjoying','enjoys',
                                                 'laughing'],
                          ['tragedy','adversity','catastrophe','pain','suffering'
                              ,'hardship','struggle','struggles','struggled','struggling','suffer','suffers','suffered'])

get_concept_count_for_all("he","she",['he','him','his','man','male','man\'s','men','boy','boys'],
                          ['she','her','her','woman','female','woman\'s','women','girl','girls'])
#concepts: love and hate
#war and peace
#victory and defeat
#happiness and tragedy
#he and she
'''

def generate_tiles():
    hsl_color1 = "hsl(33,100%,50%)"
    hsl_color2 = "hsl(215,28%,68%)"
    i=1
    j=1
    with open("concept_count.txt","r",encoding = 'utf8') as f:
        raw = f.read()
        concept_count_list = ast.literal_eval(raw)
        for concept in concept_count_list:
            print(concept[0][1]+"\n\n\n")
            for book in concept:
                ratio = float(re.findall("\d+.\d+", book[3])[0])
                hue = (215-33)*(1-ratio) + 33
                saturation = (100-28)*ratio + 28
                l_value = (68-50)*(1-ratio)+50
                if(i==j):
                    print("<tr>\n")
                    j+=3
                print("<td style =\"text-align:center; width:100px; height:100px; background-color:"+"hsl("+str(hue)+","+str(saturation)+"%,"+str(l_value)+"%)"
                +"\"><h6>"+ book[0] +"</h6></td>")
                if(i%3 ==0):
                    print("</tr>\n")
                i+=1


#generate_tiles()

def find_connections():
    #links = []
    linked_words = []
    with open("top_200_nouns.txt","r",encoding = 'utf8') as f:
        raw = f.read()
        word_list = ast.literal_eval(raw)
        i = 0
        with open("links.txt","a",encoding='utf8') as file:
            for book in word_list:
                print("Starting new book " + str(i))
                word_list_copy = ast.literal_eval(raw)
                word_list_copy[i] = ''
                for word_pair in book:
                    j = 0
                    for book_copy in word_list_copy:
                        for word_pair_copy in book_copy:
                            if word_pair[0] != "Project" and word_pair[0] != "Gutenberg" and \
                                            word_pair[0] != "Gutenberg-tm" and \
                                            word_pair[0] != "GUTENBERG-TM" and\
                                            word_pair[0].lower() == word_pair_copy[0].lower():
                                value = word_pair[1] + word_pair_copy[1]
                                value = value/100
                                #links.append({"source": i ,"target": j,"value": value})
                                if(value >= 10):
                                    file.write("{'source': +"+str(i)+" ,'target': "+str(j)+",'value': +" +str(value)+"},\n")
                                    linked_words.append(word_pair[0])
                        j+=1

                i+=1

    with open("linked_words.txt","a",encoding='utf8') as file:
        file.write(str(linked_words))

def generate_nodes():
    i =0
    for root,dirs,files in os.walk("C:/Users/Anne/IdeaProjects/BookSelfie/text"):
        for filename in files:
            print("Starting " + filename)
            full_filename = os.path.join(root, filename)
            with open("nodes.txt", "a") as f:
                f.write("{'name': +'"+filename+"' ,'group': "+str(i)+"},\n")
            i+=1

#generate_nodes()

find_connections()

#get_top_nouns_for_all()
