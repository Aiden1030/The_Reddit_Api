
#Aiden Sanghyeop Hyun
#260974945
 
 
def get_topic_comments(sub):
    '''(submission) ->  list
It takes a submission object and returns
a list of comment objects that are comments
of the submission
 
>>>url = 'https://www.reddit.com/r/mcgill/comments/eay2ne/mcgill_
                subreddit_bingo_finals_edition/'
>>>submission = reddit.submission(url=url)
>>> get_topic_comments(submission)
 
[Comment(id='fb0vh26'), Comment(id='fb0l4dk'), Comment(id='fb15bvy'),
Comment(id='fb1pwq8'), Comment(id='fb26drr'), Comment(id='fj2wd6x'),
Comment(id='fb1spzv'), Comment(id='fb1td2g'), Comment(id='fb1trul')]
 
 
>>>url=https://www.reddit.com/r/mcgill/comments/tprlmj/does_anyone_\
             know_who_is_botting_the_subreddit/
>>>submission = reddit.submission(url=url)
>>>get_topic_comments(submission)
 
[Comment(id='i2cpdml'), Comment(id='i2cpaxj'), Comment(id='i2cq6gq'),
Comment(id='i2cumjl'), Comment(id='i2cph9m'), Comment(id='i2cv1zb'),
Comment(id='i2czhbq'), Comment(id='i2cq14w'), Comment(id='i2cq8wu'),
Comment(id='i2cpuwd'), Comment(id='i2cx4tw'), Comment(id='i2cvai0'),
Comment(id='i2cr8bt'), Comment(id='i2cqh9d'), Comment(id='i2csbti')]
 
>>>url='https://www.reddit.com/r/freelance/comments/tpjfdy/do_you_send_c\
        lients_receipt_notices_when_youve/'
>>>submission = reddit.submission(url=url)
>>>get_topic_comments(submission)
 
[Comment(id='i2babqp'), Comment(id='i2bryu4'), Comment(id='i2bmcdp'),
Comment(id='i2c8bno'), Comment(id='i2c096g'), Comment(id='i2c42er'),
Comment(id='i2c8292'), Comment(id='i2crjcb')]
'''
    
    #retrieve comment ids
    
    sub.comments.replace_more(limit=None)
 
    result = sub.comments.list()
 
    return result
          
                
def filter_comments_from_authors(comm, names):
    '''(list, list) -> list
takes a list of comment objects and a list of author
names in strings as input, and returns a list containing
the comment objects that were wriiten by any of the
given authors
 
>>>url = 'https://www.reddit.com/r/mcgill/comments/paf85s/the_only_society_we_deserve/'
>>> submission = reddit.submission(url=url)
>>> comments = get_topic_comments(submission)
>>> filter_comments_from_authors(comments, ['Juan_Carl0s', 'Chicken_Nugget31'])
 
[Comment(id='ha4piat'), Comment(id='ha4j1r7')]
 
 
>>>url = 'https://www.reddit.com/r/mcgill/comments/paf85s/
the_only_society_we_deserve/'
>>> submission = reddit.submission(url=url)
>>> comments = get_topic_comments(submission)
>>> filter_comments_from_authors(comments, ['JemyFra'])
        [Comment(id='ha5mocf')]
 
 
>>> url = 'https://www.reddit.com/r/freelance/comments/tpjfdy/do_you_
send_clients_receipt_notices_when_youve/'
        submission = reddit.submission(url=url)
        comments = get_topic_comments(submission)
        filter_comments_from_authors(comments, ['Minerva1719'])
        [Comment(id='ha4chor')]
        
 
'''
    result = []
    #check comment's author name one by one
    
    for comment_id in comm:
        
        author_name = comment_id.author
        
        #add it in the list when the name matches
        
        if author_name in names:
            
            result += [comment_id]
     
    return result
            
        
 
def filter_out_comments_replied_to_by_authors(comm, authors):
    '''(list,list) -> list
takes a list of Comment objects and a list of author
names (strings) as input, and returns the same list of
Comment objects except for comments which
have been replied to by any of the authors in the given
list of authors, as well as comments written
by those authors themselves.
 
>>>>url = 'https://www.reddit.com/r/mcgill/comments/pa6ntd/does_mcgill_have_a_taylor_swift_society/'
        submission = reddit.submission(url=url)
        comments = get_topic_comments(submission)
        filter_out_comments_replied_to_by_authors(comments, ['basicbitch122'])
 
        [Comment(id='ha33z5m'), Comment(id='ha2sq62'), Comment(id='ha3d39f'),
        ...........
        Comment(id='ha2s4lw'), Comment(id='ha3mrwm'), Comment(id='i1uqddh)]
 
>>>>url = 'https://www.reddit.com/r/mcgill/comments/paf85s/the_only_society_we_deserve/'
        submission = reddit.submission(url=url)
        comments = get_topic_comments(submission)
        filter_out_comments_replied_to_by_authors(comments, ['Minerva1719'])
 
        [Comment(id='ha4piat'), Comment(id='ha4j1r7'), Comment(id='ha5mocf'),
        Comment(id='ha92bug'), Comment(id='ha4dy05'), Comment(id='ha4c6ik'),
        Comment(id='i227tfr'), Comment(id='i227x0b'), Comment(id='ha62lf9'),
        Comment(id='ha5kskb'), Comment(id='ha8fpyo'), Comment(id='i2ci2f6'),
        Comment(id='i228b5y')]
        
>>>>url='https://www.reddit.com/r/mcgill/comments/tpax2q/what_happens
_when_you_have_a_final_exam_conflict/'
         submission = reddit.submission(url=url)
         comments = get_topic_comments(submission)
         filter_out_comments_replied_to_by_authors(comments, ['steveholt81'])
        
        
        [Comment(id='i2a9nxh'), Comment(id='i2byeyw'), Comment(id='i2ab9f6'),
        Comment(id='i2a94n7'), Comment(id='i2bcjxl'), Comment(id='i2b5rlb'),
        Comment(id='i2b5ovo'), Comment(id='i2b5qk8')]
        
'''
    
    
    authors_comment_id_list = filter_comments_from_authors(comm, authors)
    
    #remove replies author wrote and its comment
    
    for i in authors_comment_id_list:
        
        #parent_id called
        
        upper_level_comment= str(i.parent_id)
        
        if 't1_' == upper_level_comment[:3]:
            
            upper_level_comment = upper_level_comment[3:]
        
        #only remove parent ID
        
        if upper_level_comment in comm:
            
            comm.remove(upper_level_comment)
        
    #remove all what the author wrote
            
    for i in authors_comment_id_list:
        
        if i in comm:
            
            comm.remove(i)
        
    
    return comm
 
 
   
 
 
def get_authors_from_topic(submission):
    '''(sub)-> dict
takes a submission as input and returns a dictionary
that has keys and values as author names and
the counts of their comments, respectively.
 
>>> url = 'https://www.reddit.com/r/mcgill/comments/pa6ntd/does_mcgill_
have_a_taylor_swift_society/'
>>> submission = reddit.submission(url=url)
>>> num_comments_per_author = get_authors_from_topic(submission)
>>> len(num_comments_per_author)
23
>>> num_comments_per_author['basicbitch122']
12
 
>>> url = 'https://www.reddit.com/r/mcgill/comments/tpax2q/what_happens_
when_you_have_a_final_exam_conflict/'
        submission = reddit.submission(url=url)
        num_comments_per_author = get_authors_from_topic(submission)
        print(num_comments_per_author)
        len(num_comments_per_author)
 
{'ChickenMcChickenFace': 1, 'steveholt81': 1, 'True_Refrigerator370': 1,
'AxFairy': 1, 'pudding-pudding': 1, 'sleepy-muggle': 1, 'Border_Andromeda': 3}
 
7
 
>>> url = 'https://www.reddit.com/r/mcgill/comments/paf85s/the_only_society_we_deserve/'
>>> submission = reddit.submission(url=url)
>>> num_comments_per_author = get_authors_from_topic(submission)
>>> len(num_comments_per_author)
8
>>> num_comments_per_author['Juan_Carl0s']
1
 
 
 
 
'''
    
    author_list = []
    
    d = {}
    
    #retrieve comments
    
    comm = get_topic_comments(submission)
    
    #get the name of the authors
    
    for comment_id in comm:
        
        author_list += [comment_id.author]
    
    
    for author in author_list:
        
        #removing deleted comments
        
        if str(author)=='None':
            
            continue
        
        #filters author's comments
        
        comments_by_author = filter_comments_from_authors(comm,[author])
        
        #count, apply, authour's name as key and int as values
        
        d[str(author)] = int(len(comments_by_author))
    
    return d
 
 
 
<strong id=line-253 class="highlight-1125959">def select_random_submission_url(reddit, url, subreddit, limit):
    
    '''(reddit, str, str, int) -> submission
 
It takes reddit object, submission link, subreddit, and
replace_more() limit. roll a dice. when 1 and 2
returns the submission object of the link and return
random submission of the subreddit for 3-6
 
 
'''
    
    import random
    
    #radomly choose a number between 1 and 6
 
    dice = random.randint(1,6)
    
    #Case 1: dice == 1 or 2:
    
    if dice == 1 or dice== 2:
         
         submission = reddit.submission(url=url)
         
         #loads the comment
         
         submission.comments.replace_more(limit=limit)
         
         return submission
    
    #Case2: dice == 3 to 6
        
    else:
        
        subreddit = reddit.subreddit(subreddit)
        
        submission_list = subreddit.top('all')
    
        random_submission_list = []
        
        #convert attribute "listing generator" to "submission"
        
        for i in submission_list:
            
            random_submission_list += [i]
        
        #choose a random submission in the list
            
        random_submission = random.choice(random_submission_list)
        
        
        
        return random_submission
    
 
 
    
def post_reply(sub,username):
    '''(submission, str)-> none
 
posts random replies in the submission given,
if the user hasn't made a comment on the submission
make a new comment'''
    
    import madlibs
    
    import random
    
    id_list = get_topic_comments(sub)
    
    author_list = []
    
    #create a list for all author's names 
    
    for comment_id in id_list:
        
        author_list += [comment_id.author]
    
    #check if user has made and replies
        
    for author in author_list:
        
        author_name = str(author)
        
        # if they did, save an object value int 0
        if author_name == username:
            
            make_a_new_top_comm = 0
            
            break
        
        # if the user hasn't made a reply int 1
        
        else:
            
            make_a_new_top_comm =1
    
    #generates a madlib sentence
            
    sentence = madlibs.generate_comment()
    
    #make a new top comment on the submission
    
    if make_a_new_top_comm == 1:
        
        sub.reply(sentence)
    #randomly choose a comment and reply to it
        
    elif make_a_new_top_comm == 0:
        
        random_comment_id= random.choice(id_list)
        
        random_comment_id.reply(sentence)
        
def bot_daemon(reddit,url,limit,subreddit,username):
    '''(reddit,string,int,string,string)->none
Combines three functions that radomly select a submission
and make a reply on reddit(1reply/1min). This function contains an
infinite loop '''
    
    import time
    
    # infinite while loop
    while 1==1:
        
        #calls these three functions non stop
        
        random_sub = select_random_submission_url(reddit, url, subreddit, limit)
        
        post_reply(random_sub,username)
        
        time.sleep(60)
        
        
        
        
        
if __name__ == '__main__':
    
    reddit = praw.Reddit('bot', config_interpolation="basic")
        
        
        
        
    
