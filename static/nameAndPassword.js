function nameAndPassword(){
    let username_make=document.getElementById("username_made")
    username_make.innerText='username is '+Username()
    let password_make=document.getElementById("password_made")
    password_make.innerText='password is '+ Userpassword() 

}

function Username(){
    let nameList=['yabsera', 'James', 'Robert', 'John', 'Michael', 'David', 'William', 'Richard', 'Joseph', 'Thomas', 'Christopher', 'Charles', 'Daniel', 'Matthew', 'Anthony', 'Mark', 'Donald', 'Steven', 'Andrew', 'Paul']
    let symbol=['_','@','#','!']
    let legth=Math.floor(Math.random()*10)
    let userName=''
    if(legth%2==0){
        userName=nameList[Math.floor(Math.random()*20)]+nameList[Math.floor(Math.random()*20)]
    }
    else{
        userName=nameList[Math.floor(Math.random()*20)]+symbol[Math.floor(Math.random()*symbol.length)]+nameList[Math.floor(Math.random()*20)]
    }
    return userName
}


function Userpassword(lengths=15){
    
    let password=''
    while(lengths>=0){

        let num=Math.floor(Math.random()*124)
        if(num>=33){
            password+=String.fromCharCode(num)
            lengths-=1;
        }
        
    }
    
   console.log(password.split(''))
   return password
}
