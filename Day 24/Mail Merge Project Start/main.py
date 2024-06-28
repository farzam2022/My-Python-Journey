#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as invited_names:
    all_names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as sample_letter:
        letter = sample_letter.read()
        for current_name in all_names:
            stripped_name = current_name.strip()
            letter.replace("[name]", stripped_name)
            with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as sending_letter:
                sending_letter.write(letter)