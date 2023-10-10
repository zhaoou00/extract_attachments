# extract_attachments

1) Use thunderbird to connect to your email through IMAP 
2) In Yahoo, create folder "home depot YYYY", search the emails from homedepot and move them to this folder. The reason is that yahoo cap the number of emails at 10,000. We aren't able to get old messages by simply searching locally.
3) create in thunderbird "Local Folders" a folder named "home depot YYYY"
4) right click the emails from 2) and "Copy to" that "home depot YYYY"folder
5) Right click that"home depot" folder and see "properties". Find the location of the file storing all the messages.
6) run my code pointing to that file to extract all attachments
