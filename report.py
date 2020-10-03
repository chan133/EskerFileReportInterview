import os

def main():

	#Have user input filepath and check if it exists
	filePath = input("Enter the file path: ")
	if os.path.exists(filePath)==False:
		print("File does not exist!")
		return

	#Open file and read its content
	f = open(filePath,'r')
	content = f.readlines()

	#Initialize variables to 0
	lineCount=0
	charCount=0
	letterCount=0
	numCount=0
	wordCount=0
	word={}

	#Each line in file
	for i in content:
		lineCount+=1

		#Each character in line
		for j in i:
			charCount +=1

			#Check what kind of character it is
			if j.isalpha():
				letterCount+=1
			elif j.isnumeric():
				numCount+=1

		#Separate each line in an array of words
		line = i.split()
		for j in line:

			#Get number of letters in the word, add/update the value in the dict
			wordLength=len(j)
			if str(wordLength) in word:
				currentVal=word[str(wordLength)]
			else:
				currentVal=0
			word[str(wordLength)]=currentVal+1

		wordCount += len(line)
	f.close()

	#Other character count is just the difference of the rest
	otherCount=charCount-letterCount-numCount

	#Write report to file
	f1 = open("report.txt",'w')
	f1.write("File name: ")
	f1.write(filePath + "\n")
	f1.write("Number of lines: ")
	f1.write(str(lineCount) + "\n")
	f1.write("Number of characters total: ")
	f1.write(str(charCount)+"\n")
	f1.write("Number of letters: ")
	f1.write(str(letterCount)+"\n")
	f1.write("Number of numbers: ")
	f1.write(str(numCount)+"\n")
	f1.write("Number of other characters: ")
	f1.write(str(otherCount)+"\n")
	f1.write("Number of words: ")
	f1.write(str(wordCount)+"\n")
	for i in sorted(word):
		f1.write("Number of %s letter words: " % i)
		f1.write(str(word[i])+"\n")
	f1.close()
	print("Report finished! Please look at report.txt to see details!")
if __name__=="__main__":
	main()