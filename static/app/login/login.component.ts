import { Component, OnInit } from '@angular/core';
import { RestClientService } from '../rest-client.service';
import { logindetails } from './logindetails';
import { Input } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
//create a variable 
login: logindetails = {username:"vthompson" , password:"123456"};

  constructor(private rest: RestClientService){} //linking rest client to login component
  //create a login function
  dologin(): void{
    console.log(this.login)
    this.rest.getlogin(this.login)
  }
  
  ngOnInit(): void {
  }

}


