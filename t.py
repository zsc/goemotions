'''
text,id,author,subreddit,link_id,parent_id,created_utc,rater_id,example_very_unclear,admiration,amusement,anger,annoyance,approval,caring,confusion,curiosity,desire,disappointment,disapproval,disgust,embarrassment,excitement,fear,gratitude,grief,joy,love,nervousness,optimism,pride,realization,relief,remorse,sadness,surprise,neutral
That game hurt.,eew5j0j,Brdd9,nrl,t3_ajis4z,t1_eew18eq,1548381039.0,1,False,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0
" >sexuality shouldn’t be a grouping category It makes you different from othet ppl so imo it fits the definition of ""grouping"" ",eemcysk,TheGreen888,unpopularopinion,t3_ai4q37,t3_ai4q37,1548084169.0,37,True,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
'''

def pack(s: str):
    ''' removes space at begining and the end, and also make sure at most 1 space between words'''
    s = s.strip()
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s

def proc(indices):
    lst = []

    for idx in indices:
        fname = f'goemotions_{idx}.csv'
        # Read a CSV file with pandas and ignore the first line
        import pandas as pd
        df = pd.read_csv(fname, skiprows=1)
        # Only keep first 10 rows
        #df = df.head(10)
        # Transform each row, by keeping only the first field, and the last 28 fields
        df = df.apply(lambda row: [row[0]] + list(row[-28:]), axis=1)
        emojis = 'admiration,amusement,anger,annoyance,approval,caring,confusion,curiosity,desire,disappointment,disapproval,disgust,embarrassment,excitement,fear,gratitude,grief,joy,love,nervousness,optimism,pride,realization,relief,remorse,sadness,surprise,neutral'.split(',')
        #print(len(emojis))
        #print(df.head(10))
        # the last 28 fields are either 0 or 1, when 0 turn into an empty string, when 1 turn into the corresponding emoji in the list above. Keep a space between adjacent emojis.
        df = df.apply(lambda row: {"instruction": "Find emotion", "input": row[0],  "output":pack(' '.join([emojis[i] if row[i+1] == 1 else '' for i in range(len(emojis))]))})
        for row in df:
            if row['output'] != '':
                lst.append(row)

    # Turn the list to a JSON file
    import json
    with open('goemotions.json', 'w') as f:
        json.dump(lst, f, indent=4)



if __name__ == '__main__':
    proc([1, 2, 3])
    
