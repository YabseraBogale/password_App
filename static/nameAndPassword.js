function nameAndPassword(){
    let make=document.getElementById("made")
    make.innerHTML='<p class="Name">'+ Username() +'</p>' + '<p class="password">'+ Userpassword() +'</p>'

}

function Username(){
    const nameList=['yabsera', 'James', 'Robert', 'John', 'Michael', 'David', 'William', 'Richard', 'Joseph', 'Thomas', 'Christopher', 'Charles', 'Daniel', 'Matthew', 'Anthony', 'Mark', 'Donald', 'Steven', 'Andrew', 'Paul']
    const symbol=['_','@','#','!']
    const legth=Math.floor(Math.random()*10)
    let userName=''
    if(legth%2==0){
        userName=nameList[Math.floor(Math.random()*20)]+nameList[Math.floor(Math.random()*20)]
    }
    else{
        userName=nameList[Math.floor(Math.random()*20)]+symbol[Math.floor(Math.random()*symbol.length)]+nameList[Math.floor(Math.random()*20)]
    }
    return userName
}


function Userpassword(length=15){
    
    let password=''
    while(length>=0){
        let num=Math.floor(Math.random()*124)
        if(num>=33){
            password+=String.fromCharCode(num)
            length--;
        }
        
    }
    return password

}

