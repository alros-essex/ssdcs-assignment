import { Component, OnInit } from '@angular/core';
import { RestClientService } from '../rest-client.service';
import { Measure } from '../measure';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {


  constructor(private rest: RestClientService){}
  //declaring a variable and get the rest service to assign measures to the variable
  //subscribe to show an error
    bleh(){
    var measures: Measure[]
    this.rest.get_measures().subscribe(m => measures = m);
    }

    ngOnInit(): void {
    }

  }



