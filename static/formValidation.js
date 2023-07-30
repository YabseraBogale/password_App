function validationForm(){
    let data=document.forms["form"]
    let sendHtml=""
    let errorCount=0
    switch(data){
        case data["website"]=="":
            sendHtml+="<li>"+"website input is empty"+"</li>"
            errorCount+=1
            case data["username"]=="":
            sendHtml+="<li>"+"user name input is empty"+"</li>"
            errorCount+=1
        case data["email"]=="":
            sendHtml+="<li>"+"email input is empty"+"</li>"
            errorCount+=1
        case data["password"]=="":
            sendHtml+="<li>"+"password input is empty"+"</li>"
            errorCount+=1
    }
    if (errorCount==0){
        return true;
    }
    else{
        let err=document.getElementById("err")
        err.innerHTML=sendHtml
        return false;
    }
     
}