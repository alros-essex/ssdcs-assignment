import { Component, OnInit } from '@angular/core';
import { RestClientService } from '../rest-client.service';
import { Experiments } from './experiments';

@Component({
  selector: 'app-experiments',
  templateUrl: './experiments.component.html',
  styleUrls: ['./experiments.component.css']
})
export class ExperimentsComponent implements OnInit {

  experiments: Experiments[] = []

  constructor(private rest: RestClientService){}
  //declaring a variable and get the rest service to assign measures to the variable
  //subscribe to show an error
    getexperiments(){
      this.rest.getexperiments().subscribe(e => this.experiments = e);  
    }
    ngOnInit(): void {
      this.getexperiments()
    }
   
  }


