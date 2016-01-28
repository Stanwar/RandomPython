import re
import nltk, string

############################################
## Main Function with Code
############################################
def codex():
        delimit = 0
        count = 1
        ############################################
        ## Initializing the Dict Variables 
        ############################################
        tokenNo = {}
        tokenCount = {}
        tokenTag = {}
        tokenBigram = {}
        tokenWordBigram = {}
        ############################################
        ## Opening File having HMM Corpus
        ############################################
        with open('assignment1.txt', 'r') as myList:
                ############################################
                ## Processing Line by Line
                ############################################

                for line in myList:

                    ############################################
                    ## Replacing PRP$ to PRPP so that NLTK can read it without problem
                    ############################################
                    try : 
                        ### Strip away non unicode
                        line = line.decode('utf-8').strip()
                        # line = line.replace("PRP$" , "PRPP") 
                        # line = line + ' /end' ## End of sentence symbol
                        xml_content = line.encode('ascii', 'xmlcharrefreplace').strip()

                        ## to print whole line
                        ##print xml_content
                    except UnicodeDecodeError:
                        print "xml_content"


                    # ############################################
                    # ## Initializing Local Variables
                    # ############################################
                    # loop = 1
                    # loop2 = 1
                    # current = ""
                    # previous = ""
                    # curr = ""
                    # prev = ""
                    # countLoop = 0

                    # ############################################
                    # ## Tokens from each line. Basically converts each word segment
                    # ############################################
                    tokens = nltk.word_tokenize(xml_content) 
                    # ############################################
                    # ## Running for Each Word Token in Each Line
                    # ############################################
                    for index in tokens:
                        #index = index.lower()
                        #print index
                        index = index.lower()
                        index = re.sub(r'\W+', '', index)
                        ###########################################
                        # Initializing the Dict with value of 0
                        ###########################################
                        tokenNo.setdefault(index,str(0))

                        tokenNo[index] = int(tokenNo[index]) + 1

                    ## Printing the complete dictionary
                #print tokenNo
                writefile = open('output.txt','w')
                for key in tokenNo:
                    print key + " " + str(tokenNo[key])
                    writefile.write(key + " " + str(tokenNo[key])  + '\n')
                
                
                    # for key in tokenNo:
                    #     print key 

                        # ############################################
                        # ## Picking bigram for likelihood probabilities of Word and the associated tag
                        # ############################################
                        # if loop2 == 1 :
                        #     prev = index
                        #     loop2 = 2

                        # else :
                        #     if countLoop%2 == 0 :
                        #         curr = index

                        #         bigr = prev + '|' + curr

                        #         tokenWordBigram.setdefault(bigr,str(0))

                        #         if tokenWordBigram[bigr] != 0:
                        #             tokenWordBigram[bigr] = int(tokenWordBigram[bigr]) + 1
                        #         prev = curr
                        #     else :
                        #         prev = index
                        #     countLoop = countLoop + 1


                        # ############################################
                        # ## Picking Tags only to calculate tag bigram 
                        # ############################################
                        # if  '/' in index:
                        #     if loop == 1 :
                        #         ### Taking /start as base case to calculate probability
                        #         previous = '/start'
                        #         current = index 

                        #         bigram = current + '|' + previous 
                        #         tokenBigram.setdefault(bigram,str(0))

                        #         if tokenBigram[bigram] != 0:
                        #             tokenBigram[bigram] = int(tokenBigram[bigram]) + 1
                        #         #print bigram + ": " + str(tokenBigram[bigram])
                        #         loop = 2
                        #     else :
                        #         previous = current 
                        #         current = index

                        #         bigram = current + '|' + previous  
                        #         tokenBigram.setdefault(bigram,str(0))

                        #         if tokenBigram[bigram] != 0:
                        #             tokenBigram[bigram] = int(tokenBigram[bigram]) + 1
                        #         #print bigram + ": " + str(tokenBigram[bigram])



                # #print tokenWordBigram
                
                # #####################################################
                # ## Count of Tags in Corpus
                # #####################################################
                # for key in tokenNo:
                #     if  '/' in key:
                #         tokenTag[key] = tokenNo[key]
                # ## Count of the number of sentences        
                #     print tokenTag

                # #####################################################
                # ## Tag Bigram Probability
                # #####################################################
                
                # writefile = open('tagBigram.txt','w') ## File with tag Bigram

                # for key in tokenBigram:
                #     previous = key[ int(key.index('|') + 1) : int(len(key))]
                #     #print 1/3
                #     #print "previous : " + previous
                #     #print "key" + key + "tokenBigram[key]"  + str(tokenBigram[key]) + "int(tokenTag[previous])" + str(tokenTag[previous])
                #     #print "P(" + str(key) + ") : " +  str(float(tokenBigram[key])/float(tokenTag[previous]))
                #     printVariable = "P(" + str(key) + ") : " +  str(float(tokenBigram[key])/float(tokenTag[previous]))

                #     ## Printing to File 
                #     writefile.write(printVariable  + '\n')


                # #####################################################
                # ## Likelihood Probility in Corpus
                # #####################################################
                # writefile = open('lexicalProbability.txt','w') ## File with lexical Probability

                # for key in tokenWordBigram:
                #     previous = key[ int(key.index('|') + 1) : int(len(key))]
                #     #print "key" + key + "tokenWordBigram[key]"  + str(tokenWordBigram[key]) + "int(tokenTag[previous])" + str(tokenTag[previous])
                #     #print "P(" + str(key) + ") : " +  str(float(tokenWordBigram[key])/float(tokenTag[previous]))
                #     printVariable = "P(" + str(key) + ") : " +  str(float(tokenWordBigram[key])/float(tokenTag[previous]))
                #     writefile.write(printVariable  + '\n')



                    

if __name__ == "__main__":
    codex()
                      
