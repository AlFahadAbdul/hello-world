text_one= "the cleveland cavs are a horrible side; lebron james is literally\
 carrying them on his shoulders. i hope they beat the celtics for his legacy,\
 for me he's already the greatest."
def clean_text(input):
    input =input.replace(";",".")
    input = input.replace(",", ", ")
    input = input.split(".")
    output=""
    del input[-1]
    for text in input:
        text = text.lstrip()
        text = text.capitalize()
        text = text + "."
        output = output + text 

    print(output)

clean_text(text_one)



    
    
    

    


    

    
    
    





    

