NOTE Example 4.2: A better conditional message
    TELL 'Would you like to see a message? (y/n)'
10  ASK response
11  TELL 'Hello, world!' NEXT
 9  NOTE Dummy label
    COME FROM 10 + SGN(response - "n")