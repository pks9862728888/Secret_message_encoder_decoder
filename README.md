# Secret_message_encoder
This script encodes the message by letters in the picture and subsequently renames the picture by randomly generated numbers. Also deletes the extension and adds a fake extensions which are by-default hidden in Windows. Also changes pictures to hidden to completely encode the message. 

## Execution instructions
- For encoding message, only alphanumeric characters, blank space and dot(.) are allowed.
- For decoding message, the message folder should be placed in the folder from where the script is run. This ensures automatic detection of the Encoded messages folder. Else you will have to manually mention the location of encoded messages folder.

### Working of Encoder.py
- First user is prompted to enter a message.

![Enter message](https://github.com/pks9862728888/Secret_message_encoder/blob/master/Screenshots/Encoder%2000.png)

- Then the message is scanned for invalid characters(*if any*).
- If invalid charactes are found then asked whether to encode the message by removing the invalid characters?
- If user doesn't want to encode the message, then he can re-enter a new message.

![Remove Invalids](https://github.com/pks9862728888/Secret_message_encoder/blob/master/Screenshots/Encoder%2001.png)

- If the user choses to encode the message, then the message is encoded.

![Encoding status](https://github.com/pks9862728888/Secret_message_encoder/blob/master/Screenshots/Encoder%2002.png)

Each letter is encoded with a picture and subsequently the names are scrumbled and the pictures are hidden.

Output folder: *Encoded_message_output*

If already a folder exists, then new output folder name is created.

### Encoding process
Encoding the message is done by words present in *word_names.txt* file. If this file is not found, then the words are fetched from the internet from *word_names.txt* file present in this repository of GitHub.

The encoding is done in three steps:
1. First a random number is generated and then a random seed is generated to determine where the number will be inserted in encodable file name.
2. Then after each character in new file name a random number is added.
3. Then *.jpg* extention is removed and fake extentions are added to the pictures.
4. Finally a dot(.) is added to each picture names to render the letters invisible.
5. Then the letters are renamed in output folder.

![Output Folder After Encoding: Encoded_message_output](https://github.com/pks9862728888/Secret_message_encoder/blob/master/Screenshots/Output%20after%20Encoding.png)

### Working of Decoder.py
Decoding process is exactly opposite to that of Encoder.py. This script outputs the decoded the message in the source encoded message folder.

![Selecting encoded message](https://github.com/pks9862728888/Secret_message_encoder/blob/master/Screenshots/Decoder%2000.png)
![Decoding message](https://github.com/pks9862728888/Secret_message_encoder/blob/master/Screenshots/Decoder%2001.png)

### Decoding process
1. First the fake extention is removed.
2. Then all the characters except A-Z and a-z are removed.
3. Then the correct extention .jpg is added.
4. Then the files are renamed in source folder

![Output Folder After Decoding](https://github.com/pks9862728888/Secret_message_encoder/blob/master/Screenshots/Output%20after%20Decoding.png)

**Please suggest edits to improve the code. Thank you for your valuable time.**
