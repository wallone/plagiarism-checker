# plagiarism-checker

The goal of this file is to produce a ranked list of pairwise assignment pairs such that the first pair of python files is the most similar and the last pair of python files is the least similar using the Linux wdiff command. This allows the comparison of  two files for textual similarity. To test this code, create python files and populate arrayA and arrayB with the names of these files. Both files should be populated with the same array.

Follow the steps below to duplicate.

INSTALL wdiff
==============
	1.	Press Command+Space and type Terminal and press enter/return key.
	2.	Run in Terminal app:
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
and press enter/return key. Wait for the command to finish.
	3.	Run:
brew install wdiff

copy files to be compared to the same path where this will be run.(I have included the files with my zipped files)



The first thing I did when working was to create two dummy files and ran my wdiff from my terminal to see how it worked. I chose wdiff(instructions on installing wdiff on a mac are below) because of the parameter that gives statistics based on the comparison of two files. After figuring out how this worked, I then learnt how to run linux command from my python IDE. For reference on how to do this, I used the site http://stackoverflow.com/questions/9735863/running-a-linux-command-from-python.

Below are the steps .
===========================
I imported subprocess to enable me to run linux command
I imported operator to enable sorting as results are to be ranked.

I created 2 arrays of the same content(files to be compared). I did this that way I have 2 loops I can run. The first loop can be considered as the parent loop and the second loop the child loop. I pick the first file in the parent loop and run it against all the files in the child loop excepts its self. I have a condition that filter out and comparison if the file name of the parent array is similar to that of the child array. That is, 1.py will not compare against 1.py because they are the same file. Once this step is passed and the two files are not deemed identical, I then proceed to insert the information of both files in array that way we can check against that array and not run it if that pair exists in this array. I also swapped the position of both files that way it does not run the inverse. Example, comparing 1.py and 2.py is the same as comparing 2.py and 1.py. Therefore my validation array contains [1.py,2.py] and [2.py,1.py] hence this comparison for both files is only ran once.

Now that I have this in place, I now format my comparison string(ex. wdiff -si123 1.py 2.py ). This returns the result of the comparison. I filter out the information with the ‘%’ as this is the information I am interest in. This information provides how similar the two compared files are.

I then create an array using the two file names I have compared as the key and the percentage of similarity as the value.

Once this is created for all the files, I sort this information, loop through this information and create a nicely formatted string that tells us what that comparison of each file is to the others sorted in descending order. 

