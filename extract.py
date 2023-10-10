import mailbox, pdb
def extractattachements(message, path = r'C:\Users\cubla\Downloads\homedepot 2021\ '[:-1]):
    if message.get_content_maintype() == 'multipart':
        for part in message.walk():
            if part.get_content_maintype() == 'multipart': continue
            if part.get('Content-Disposition') is None: continue
            filename = path+message['Date'].replace(':','-')+'_'+part.get_filename()
            print (filename)
            fb = open(filename,'wb')
            fb.write(part.get_payload(decode=True))
            fb.close()
mbox = mailbox.mbox(r'C:\Users\cubla\AppData\Roaming\Thunderbird\Profiles\njlwv0k2.default-release\Mail\Local Folders\home depot 2021')
for message in mbox:
    extractattachements(message)
    
