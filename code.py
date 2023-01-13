class Solution:
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)] # left align the string, using a specified character (space is default) as the fill character

      
      '''
How does it work? Well in the question statement, the sentence "Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words,
 the empty slots on the left will be assigned more spaces than the slots on the right" was just a really long and awkward way to say round robin. 

for i in range(maxWidth - num_of_letters):
                cur[i%(len(cur)-1 or 1)] += ' '
What does this line do? Once you determine that there are only k words that can fit on a given line, you know what the total length of those words is num_of_letters. 
Then the rest are spaces, and there are (maxWidth - num_of_letters) of spaces. The "or 1" part is for dealing with the edge case len(cur) == 1.
'''
      
      
      
      
