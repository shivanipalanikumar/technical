import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  // public firstname:string="John";
  // public lastname:string="Stoke";
  // public Salary:number=5000;
  // public permanentstaff:boolean=true;
  employee={
    fname:'Shivani',
    lname:'P',
    Salary:10800,
    staff:true,
    department:{id:3,name:'Payroll'},
    skills:[{id:'1',value:'HTML'},{id:'2',value:'CSS'},{id:'3',value:'JavaScript'}]
  }//object
  constructor(){
    //console.log(this.Salary,this.firstname,this.lastname,this.permanentstaff);//my understanding
    console.log(this.employee);//hands on one

    //hands on 2
    console.log('fname: '+ this.employee.fname);
    console.log('lname: '+ this.employee.lname);
    console.log('Salary: '+ ((this.employee.Salary).toString()));
    console.log('Staff: '+((this.employee.staff).toString()));

    //hands on 3
    console.log('departmentid: '+((this.employee.department.id).toString()));
    console.log('departmentname: '+ this.employee.department.name);
    for(let i=0;i<3;i++){
      let j=i+1;
      console.log('skill '+ j +': '+(this.employee.skills[i].id).toString()+ ', ' +this.employee.skills[i].value);
    }
  }
}


// First Name John String
// Last Name Stoke String
// Salary 5000 Number
// Permanent
// Staff true Boolean
