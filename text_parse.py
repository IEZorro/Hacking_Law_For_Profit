#Making it so that our for loop goes through lines themselves and not individual characters so that we may parse easily using Regex.
create = open('txt/pdf_txt/DataScience.pdf.txt', 'r')
for line in create:
    #Regex Here
    print(line)
