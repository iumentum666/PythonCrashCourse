magicians = ['alice','david','carolina']

# Her lager vi en for loop som lister opp alle verdiene i listen0
for magician in magicians:
    # print(magician) #simpel opplisting
    print(magician.title()+ ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n") # man kan ha flere linjer med kode i en loop

print("Thank you, everyone. That was a great magic show!") # Den første linjen som ikke er indented er slutten på loopen, og blir bare gjort en gang