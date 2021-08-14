import praw
from psaw import PushshiftAPI
import pdb
import re
import os
import time
import sys
import pickledb

def main():
    time.sleep(60)
    r = praw.Reddit('bot1')
    api = PushshiftAPI(r)

    gen = api.search_comments(q=r"major problem", subreddit='bottestformeonly', metadata= True)

    max_response_cache = 1000
    cache = []
    
    db = pickledb.load('comments_replied_to.db', False)
   
    filtered_comments = []
    test_count = 0
    for c in gen:
        cache.append(c)
        if re.search("major problem", c.body.lower(), re.IGNORECASE):
            filtered_comments.append(c)

        if len(cache) >= max_response_cache:
            break

    for c in filtered_comments:
        for i in range(1):
            if c.author == 'MajorProblem_bot':
                print('MajorProblem_bot post detected.\nSkipped.')
                break
            body_as_string = c.body
            if db.get(body_as_string) == c.author:
                print('Detected a chat that has already been replied to.\nSkipped.')
                break
            else:

                print(f'just beginning: {c.name}')
                finalsplitlist = []
                splitlist = re.split('\W+', c.body)
                for i in splitlist:
                    finalsplitlist.append(i.lower())
 

                outputlist = re.split('\W+', c.body)
                newline = '\n'
                major_index = int(finalsplitlist.index("major"))
            
                quote = f"""> {outputlist[major_index].strip(newline)} {outputlist[major_index+1].strip(newline)}"""

                print(quote)
        
                c.reply(f"""{quote}

*salute*
\nMAJOR PROBLEM\n

---------------
^(Hi,) ^(I'm) ^(a) ^(bot.) ^(I) ^(was) ^(built) ^(for) ^(fun) | [Learn More](https://zachcohn.me/majorproblembot) | [opt out](https://zachcohn.me/majorproblembot/optout?user={c.author})
""")
                body_string = str(c.body)
                username = str(c.author)
                db.set(body_string, username)
                db.dump()
                print("just posted a comment! Now I'm going to take a nap.")
                time.sleep(360)

while True:
    main()
