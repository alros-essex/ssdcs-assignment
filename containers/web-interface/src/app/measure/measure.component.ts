import { Component, OnInit } from '@angular/core';
import { RestClientService } from '../rest-client.service';
import { Measure } from '../measure';
@Component({
  selector: 'app-measure',
  templateUrl: './measure.component.html',
  styleUrls: ['./measure.component.css']
})
export class MeasureComponent implements OnInit {

  constructor(private rest: RestClientService){}
//declaring a variable and get the rest service to assign measures to the variable
//subscribe to show an error
  bleh(){  
  var measures: Measure[]
  this.rest.getmeasures().subscribe(m => measures = m);
  }

  ngOnInit(): void {
  }
 
}
