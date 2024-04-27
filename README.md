Generating randomness game.

<p>Initially, the player has a virtual balance of $1000. Every time the computer guesses a symbol correctly, the player loses one dollar. Every time the system is wrong, the player gets one dollar.</p><br/><br/></a>

<b>EXAMPLE</b>

Please provide AI some data to learn...<br/>
The current data length is 0, 100 symbols left<br/>
Print a random string containing 0 or 1:<br/>

> 010100100101010101000010001010101010100100100101001<br/>
The current data length is 51, 49 symbols left<br/>
Print a random string containing 0 or 1:<br/>

> 011010001011111100101010100011001010101010010001001010010011<br/>

Final data string:<br/>
010100100101010101000010001010101010100100100101001011010001011111100101010100011001010101010010001001010010011<br/>

You have $1000. Every time the system successfully predicts your next press, you lose $1.<br/>
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!<br/>

Print a random string containing 0 or 1:<br/>

> 0111001001<br/>
predictions:<br/>
0101011<br/>

Computer guessed 4 out of 7 symbols right (57.14 %)<br/>
Your balance is now $999<br/>

Print a random string containing 0 or 1:<br/>

> some wrong input<br/>

Print a random string containing 0 or 1:<br/>

> 0101001001<br/>
predictions:<br/>
1011011<br/>

Computer guessed 5 out of 7 symbols right (71.43 %)<br/>
Your balance is now $996<br/>

Print a random string containing 0 or 1:<br/>

> enough<br/>
Game over!<br/>
