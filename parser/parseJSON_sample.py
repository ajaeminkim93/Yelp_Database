import json

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def parseBusinessData():
    #read the JSON file
    with open('./yelp_business.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('./business.txt', 'w')
        line = f.readline()#each line contains a json
        count_line = 0
        days = ["Monday","Tuesday",'Wednesday','Thursday','Friday']
        #read each JSON abject and extract data        
        while line:
            data = json.loads(line)            
            outfile.write(str(count_line) + '\n')
            #print(count_line)
            '''if count_line == 0:
                print(data)'''
            #print(data)    

            #'\t is for tab
            outfile.write(cleanStr4SQL(data['business_id'])+'\t') #business id
            outfile.write(cleanStr4SQL(data['name'])+'\t') #name
            outfile.write(cleanStr4SQL(data['address'])+'\t') #full_address
            outfile.write(cleanStr4SQL(data['state'])+'\t') #state
            outfile.write(cleanStr4SQL(data['city'])+'\t') #city
            outfile.write(cleanStr4SQL(data['postal_code']) + '\t')  #zipcode
            outfile.write(str(data['latitude'])+'\t') #latitude
            outfile.write(str(data['longitude'])+'\t') #longitude
            outfile.write(str(data['stars'])+'\t') #stars
            outfile.write(str(data['review_count'])+'\t') #reviewcount
            outfile.write(str(data['is_open'])+'\t') #openstatus

            categories = data["categories"].split(', ')
            outfile.write(str(categories)+'\t')  #category list
            

            #MY CODE

            #My code for Attributes
            #outfile.write(str([])) # write your own code to process attributes
            attributes = data['attributes']
            if len(attributes) != 0:
                outfile.write(str("Attributes:["))
                helper(attributes,outfile)
                '''length = len(attributes)
                index = 0
                for att in attributes:
                    outfile.write('(' +str(att) + ' : ')                    
                    outfile.write(str(attributes[att]) + ')')
                    index += 1
                    if index < length:
                        outfile.write(',')
                '''
                outfile.write(str("]\t"))
                


            #my code for HOURS for each day
            hours = data['hours']
            for day in days:
                if day in hours:
                    outfile.write(str(day) + ' : ')
                    outfile.write(str(hours[day]) + '\t')

            #outfile.write(str([])) # write your own code to process hours
            outfile.write('\n\n\n');

            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()

#if a key value is a json
def helper(obj,outfile):        
    for key,val in obj.items():            
        if type(val) == dict:#if it is a json, recursively call this function
            helper(val,outfile)
        else:            
            outfile.write('({} : {})\t'.format(key,val))#else we just print out this pair.

def parseUserData():
    #write code to parse yelp_user.JSON
    with open('./yelp_user.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('./user.txt', 'w')
        line = f.readline()#each line contains a json
        count_line = 0                
        while line:
            data = json.loads(line)            
            outfile.write(str(count_line) + '\n')            
            helper(data,outfile)                    
            outfile.write('\n\n\n');
            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()

def parseCheckinData():
    #write code to parse yelp_checkin.JSON
    with open('./yelp_checkin.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('./checkin.txt', 'w')
        line = f.readline()#each line contains a json
        count_line = 0        
        #read each JSON abject and extract data        
        while line:
            data = json.loads(line)                      
            outfile.write(str(count_line) + '\n')
            outfile.write('({} : {})\n'.format('business_id',data['business_id']))

            #for date, we need to split the timestamps
            dates = data['date']
            count = 0   #var used to count how many dates we should output per line.
            for date in dates.split(','):

                time_stamp = date.split(' ')#after split, date will be a list of two elements.
                day_month_year = time_stamp[0]
                time = time_stamp[1]
                outfile.write('({} : {})'.format(day_month_year, time))
                count += 1

                if count == 2:
                    count = 0
                    outfile.write('\n')

                else:
                    outfile.write('\t\t')                
                   
            outfile.write('\n\n\n');
            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()


def parseTipData():
    #write code to parse yelp_tip.JSON
    with open('./yelp_tip.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('./tip.txt', 'w')
        line = f.readline()#each line contains a json
        count_line = 0        
        #read each JSON abject and extract data        
        while line:
            data = json.loads(line)            
            outfile.write(str(count_line) + '\n')
            helper(data,outfile)
            outfile.write('\n\n\n');

            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()

parseBusinessData()
parseUserData()
parseCheckinData()
parseTipData()
