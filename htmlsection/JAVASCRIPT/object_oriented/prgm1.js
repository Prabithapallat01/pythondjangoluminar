class Student{
    setStudent(rol,name,marks){
        this.rol=rol
        this.name=name
        this.marks=marks
    }
    printStudent(){
        console.log(this.rol+","+this.name+","+this.marks);
    }
}
var obj=new Student();
obj.setStudent(12,"sam",345);
obj.printStudent();
