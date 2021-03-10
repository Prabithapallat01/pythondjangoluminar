//  FIBONACCI SERIES:



var num=0;
var a=0;
var b=1;
var count=0;

if(num<=0){
    console.log("Enter positive number:");
}
else{
    while(count<num){
        console.log(a);
        var c=a+b;
        a=b;
        b=c;
        count+=1;
    }
}