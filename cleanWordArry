// Cleans and converts the textfield into an array
function main(inputstring) {
        str = inputstring.toLowerCase();

        reg0 = /(@\S+|#\S+|https\S+|\n)/ig;  //Replace mentions, hashtags and Url
        str = str.replace(reg0, " ");

        str = str.replace(" ", " abc ");     //with stopwords directly after each other only the first is remowed therefore inserting fakewords

        reg1 = /[^a-zA-ZåäöÅÄÖ\s]/ig;      //Replace all non characters or numbers
        str = str.replace(reg1, " ");   

        str = " " + str + " ";                //Add space to begining and end of string

        reg = /\s(rt|aldrig|alla|allt|alltid|alltså|andra|annat|att|av|amp)\s/ig;
        str = str.replace(reg, " "); 
        reg = /\s(bara|barn|behöver|bilder|blev|bli|blir|blivit|borde|bort|bra|både|bästa|bättre|börjar)\s/ig;
        str = str.replace(reg, " "); 
        reg = /\s(dag|dagen|dagens|dags|de|del|dem|den|denna|deras|dessa|det|detta|dig|din|dom|dra|du|då|där)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(efter|eller|emot|en|enda|ens|er|ett)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(fan|februari|fel|fick|finns|fler|flera|folk|fortfarande|fram|från|få|får|fått|för|första|förstår)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(ge|genom|ger|gick|gjort|gå|gång|går|gärna|gör|göra)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(ha|hade|han|har|hej|hela|heller|helt|hem|hon|honom|hoppas|hos|hur|håller|här|höra)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(idag|igen|igår|inför|ingen|inga|inget|innan|inom|inte|is|ja|jag|ju|just|jävla)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(kan|kanske|kom|kommer|kr|kul|kunna|kvar|känna|känner|känns|kör)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(lade|ligger|lika|lite|liv|livet|loch|läs)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(man|med|mellan|men|mer|mest|mig|min|mina|mitt|mot|mycket|mål|många|måste|människor)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(nej|ner|ni|nog|nu|ny|nya|nytt|någon|något|några|nån|när|nästa)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(och|också|om|oss|pga|plats|precis|på|redan|riktigt|runt|rätt)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(sa|saker|samma|se|sedan|sen|senaste|ser|sett|sex|sig|sin|sina|sista|sitt|sitter|själv|ska|skulle|snart|som|stor|stora|straff|står|svar|svenska|svensk|sverige|sveriges|svårt|så|såg|säga|säger|söndag)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(ta|tack|tar|the|tid|till|tillbaka|tog|tre|tror|två|typ|tycker|under|undrar|upp|ut|utan)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(va|vad|var|vara|varför|varit|varje|vem|verkar|verkligen|vet|vi|vid|video|vilka|vilken|vilket|vill|vår|våra|väl|väldigt)\s/ig;
        str = str.replace(reg, " ");
        reg = /\s(åka|år|åt|än|ändå|är|även|över)\s/ig;
        str = str.replace(reg, " ");

        str = str.replace("abc", "");        //Remove fake words

        reg = /[ ][a-zå-ö][ ]/;				 //Testas
		str = str.replace(reg, " ");

        reg4 = /(\s+)/                       //replace all extra blankspaces
        str = str.replace(reg4, " ")

        arr= str.trim().split(" ");
    return arr;
